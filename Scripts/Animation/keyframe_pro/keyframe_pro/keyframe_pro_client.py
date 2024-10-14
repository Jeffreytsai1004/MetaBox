import json
import socket
import time
import traceback


class KeyframeProClient(object):
    """
    Client API for Keyframe Pro
    """

    API_VERSION = "1.0.1"

    PORT = 18181

    HEADER_SIZE = 10

    kpro_socket = None
    kpro_initialized = False

    def __init__(self, timeout=2):
        """
        """
        self.timeout = timeout
        self.show_timeout_errors = True

    def connect(self, port=-1, display_errors=True):
        """
        Create a connection with the application.

        :param port: The port Keyframe Pro is listening on.
        :return: True if connection was successful (or already exists). False otherwise.
        """
        if self.is_connected():
            return True

        if port < 0:
            port = self.__class__.PORT

        try:
            self.__class__.kpro_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__class__.kpro_socket.connect(("localhost", port))
            self.__class__.kpro_socket.setblocking(0)

            self.__class__.kpro_initialized = False

        except:
            self.__class__.kpro_socket = None
            if display_errors:
                traceback.print_exc()
            return False

        return True

    def disconnect(self):
        """
        Disconnect from the application.

        :return: True if the existing connection was disconnect successfully. False otherwise.
        """
        result = False
        if self.__class__.kpro_socket:
            try:
                self.__class__.kpro_socket.close()
                result = True
            except:
                traceback.print_exc()

        self.__class__.kpro_socket = None
        self.__class__.kpro_initialized = False

        return result

    def is_connected(self):
        """
        Test if a connection exists.

        :return: True if a connection exists. False otherwise.
        """
        self.show_timeout_errors = False
        connected = self.__class__.kpro_socket and self.echo("conn")
        self.show_timeout_errors = True

        if connected:
            return True
        else:
            self.disconnect()
            return False

    def send(self, cmd):
        """
        Send a command to the application and wait for a processed reply.

        :param cmd: Dictionary containing the cmd and args
        :return: Variable depending on cmd.
        """
        json_cmd = json.dumps(cmd)

        message = []
        message.append("{:10d}".format(len(json_cmd)))  # header
        message.append(json_cmd)

        try:
            self.__class__.kpro_socket.sendall("".join(message))
        except:
            traceback.print_exc()
            return None

        return self.recv(cmd)

    def recv(self, cmd):
        """
        Wait for the application to reply to a previously sent cmd.

        :param cmd: Dictionary containing the cmd and args
        :return: Variable depending on cmd.
        """
        total_data = []
        data = ""
        reply_length = 0
        bytes_remaining = self.__class__.HEADER_SIZE

        begin = time.time()
        while time.time() - begin < self.timeout:

            try:
                data = self.__class__.kpro_socket.recv(bytes_remaining)
            except:
                time.sleep(0.01)
                continue

            if data:
                total_data.append(data)

                bytes_remaining -= len(data)
                if(bytes_remaining <= 0):

                    if reply_length == 0:
                        header = "".join(total_data)
                        reply_length = int(header)
                        bytes_remaining = reply_length
                        total_data = []
                    else:
                        reply_json = "".join(total_data)
                        return json.loads(reply_json)

        if self.show_timeout_errors:
            if "cmd" in cmd.keys():
                cmd_name = cmd["cmd"]
                print('[KPRO][ERROR] "{0}" timed out.'.format(cmd_name))
            else:
                print('[KPRO][ERROR] Unknown cmd timed out.')

        return None

    def is_valid_reply(self, reply):
        """
        Test if a reply from the application is valid. Output any messages.

        :param reply: Dictionary containing the response to a cmd
        :return: True if valid. False otherwise.
        """
        if not reply:
            return False

        if not reply["success"]:
            print('[KPRO][ERROR] "{0}" failed: {1}'.format(reply["cmd"], reply["msg"]))
            return False

        return True

    def initialize(self):
        """
        One time initialization required by the application.

        :return: True if successfully initalized. False otherwise.
        """
        if self.__class__.kpro_initialized:
            return True

        cmd = {
            "cmd": "initialize",
            "api_version": self.__class__.API_VERSION
        }

        reply = self.send(cmd)
        if reply and reply["success"] and reply["result"] == 0:
            self.__class__.kpro_initialized = True
            return True
        else:
            print('[KPRO][ERROR] Initialization failed: {0}'.format(reply["msg"]))
            self.disconnect()
            return False

    # ------------------------------------------------------------------
    # COMMANDS
    # ------------------------------------------------------------------
    def echo(self, text):
        """
        Get an echo response from the application.

        :param text: The string to be sent to the application.
        :return: A string containing the text on success. None otherwise.
        """
        cmd = {
            "cmd": "echo",
            "text": text
        }

        reply = self.send(cmd)
        if self.is_valid_reply(reply):
            return reply["result"]
        else:
            return None

    def get_config(self):
        """
        Get the configuration settings for the application.

        :return: Dictionary containing the config values.
        """
        cmd = {
            "cmd": "get_config"
        }

        reply = self.send(cmd)
        if self.is_valid_reply(reply):
            return reply
        else:
            return None

    def new_project(self, empty=False):
        """
        Create a new project.

        :param empty: Create an empty project.
        :return: True if new project created. False otherwise.
        """
        cmd = {
            "cmd": "new_project",
            "empty": empty
        }

        reply = self.send(cmd)
        if self.is_valid_reply(reply):
            return True
        else:
            return False

    def open_project(self, file_path):
        """
        Open an existing project.

        :param file_path: Path to the project.
        :return: True if the project is opened. False otherwise.
        """
        cmd = {
            "cmd": "open_project",
            "file_path": file_path
        }

        reply = self.send(cmd)
        if self.is_valid_reply(reply):
            return True
        else:
            return False

    def save_project(self, file_path):
        """
        Save the current project.

        :param file_path: Path to the project.
        :return: True if the project is saved. False otherwise.
        """
        cmd = {
            "cmd": "save_project",
            "file_path": file_path
        }

        reply = self.send(cmd)
        if self.is_valid_reply(reply):
            return True
        else:
            return False

    def get_project_path(self):
        """
        Get the path to the current project.

        :return: The path to the project. None if there is an error.
        """
        cmd = {
            "cmd": "get_project_path"
        }

        reply = self.send(cmd)
        if self.is_valid_reply(reply):
            return reply["project_path"]
        else:
            return None

    def import_file(self, file_path, name="", range_start=-1, range_end=-1, parent_id=""):
        """
        Import a source file into the project.

        :param file_path: Path to the source
        :param name: Name of the source
        :param range_start: Range start frame
        :param range_end: Range end frame
        :param parent_id: Parent folder of the source
        :return: Dictionary representing the source object. None on error.
        """
        cmd = {
            "cmd": "import_file",
            "file_path": file_path,
            "name": name,
            "range_start": range_start,
            "range_end": range_end,
            "parent_id": parent_id
        }

        reply = self.send(cmd)
        if self.is_valid_reply(reply):
            return reply["source"]
        else:
            return None

    def add_folder(self, name="", parent_id=""):
        """
        Add a folder to the project.

        :param name: Name of the folder
        :param parent_id: Parent folder of the folder
        :return: Dictionary representing the folder object. None on error.
        """
        cmd = {
            "cmd": "add_folder",
            "name": name,
            "parent_id": parent_id
        }

        reply = self.send(cmd)
        if self.is_valid_reply(reply):
            return reply["folder"]
        else:
            return None

    def add_timeline(self, name="", parent_id=""):
        """
        Add a timeline to the project.

        :param name: Name of the timeline
        :param parent_id: Parent folder of the timeline
        :return: Dictionary representing the timeline object. None on error.
        """
        cmd = {
            "cmd": "add_timeline",
            "name": name,
            "parent_id": parent_id
        }

        reply = self.send(cmd)
        if self.is_valid_reply(reply):
            return reply["timeline"]
        else:
            return None

    def remove(self, id, force=False):
        """
        Remove a folder, timeline or source from the project.

        :param id: ID for the object to be removed.
        :param force: (Source only) Force removal if the source is in use in one or more timelines.
        :return: True on successful removal. False otherwise.
        """
        cmd = {
            "cmd": "remove",
            "id": id,
            "force": force
        }

        reply = self.send(cmd)
        if self.is_valid_reply(reply):
            return True
        else:
            return False

    def update(self, obj):
        """
        Update the folder, timeline or source object with the values contained in the obj dict.
        Editable obj values that are different will be modified.

        :param obj: Dictionary representing the object to be updated.
        :return: Dictionary representing the updated object. None on error.
        """
        cmd = {
            "cmd": "update",
            "object": obj
        }

        reply = self.send(cmd)
        if self.is_valid_reply(reply):
            return reply["updated"]
        else:
            return None

    def insert_element_in_timeline(self, source_id, timeline_id, index=-1):
        """
        Insert a source element into a timeline.

        :param source_id: ID of the source to be added to the timeline.
        :param timeline_id: ID of the timeline.
        :param index: Index to insert source at. Inserted at the end if index is out of range.
        :return: True on successful insertion. False otherwise.
        """
        cmd = {
            "cmd": "insert_element_in_timeline",
            "source_id": source_id,
            "timeline_id": timeline_id,
            "index": index
        }

        reply = self.send(cmd)
        if self.is_valid_reply(reply):
            return True
        else:
            return False

    def remove_element_from_timeline(self, timeline_id, index):
        """
        Remove a source element from a timeline.

        :param timeline_id: ID of the timeline.
        :param index: Index of the element to be removed.
        :return: True on successful removal. False otherwise.
        """
        cmd = {
            "cmd": "remove_element_from_timeline",
            "timeline_id": timeline_id,
            "index": index
        }

        reply = self.send(cmd)
        if self.is_valid_reply(reply):
            return True
        else:
            return False

    def get_timeline_elements(self, timeline_id):
        """
        Get an ordered list of the sources in a timeline.

        :param timeline_id: ID of the timeline.
        :return: An ordered list of dictionaries representing the sources in a timeline. None on error.
        """
        cmd = {
            "cmd": "get_timeline_elements",
            "timeline_id": timeline_id
        }

        reply = self.send(cmd)
        if self.is_valid_reply(reply):
            return reply["sources"]
        else:
            return None

    def get_folders(self):
        """
        Get an unordered list of the folders in the project.

        :return: An unordered list of dictionaries representing the folders in the project. None on error.
        """
        cmd = {
            "cmd": "get_folders"
        }

        reply = self.send(cmd)
        if self.is_valid_reply(reply):
            return reply["folders"]
        else:
            return None

    def get_timelines(self):
        """
        Get an unordered list of timelines in the project.

        :return: An unordered list of dictionaries representing the timelines in the project. None on error.
        """
        cmd = {
            "cmd": "get_timelines"
        }

        reply = self.send(cmd)
        if self.is_valid_reply(reply):
            return reply["timelines"]
        else:
            return None

    def get_sources(self):
        """
        Get an unordered list of sources in the project.

        :return: An unordered list of dictionaries representing the sources in the project. None on error.
        """
        cmd = {
            "cmd": "get_sources"
        }

        reply = self.send(cmd)
        if self.is_valid_reply(reply):
            return reply["sources"]
        else:
            return None

    def get_frame(self):
        """
        Get the current frame of the (primary) active timeline.

        :return: The frame of the (primary) active timeline. Zero on error.
        """
        cmd = {
            "cmd": "get_frame"
        }

        reply = self.send(cmd)
        if self.is_valid_reply(reply):
            return reply["frame"]
        else:
            return 0

    def set_frame(self, frame, audio=False):
        """
        Set the current frame of the (primary) active timeline.

        :param frame: Requested frame number
        :param audio: Play audio for the frame after setting it.
        :return: The frame of the (primary) active timeline. Zero on error.
        """
        cmd = {
            "cmd": "set_frame",
            "frame": frame,
            "audio": audio
        }

        reply = self.send(cmd)
        if self.is_valid_reply(reply):
            return reply["frame"]
        else:
            return 0

    def get_range(self):
        """
        Get the current range of the (primary) active timeline.

        :return: Tuple containing the range of the (primary) active timeline. None on error.
        """
        cmd = {
            "cmd": "get_range"
        }

        reply = self.send(cmd)
        if self.is_valid_reply(reply):
            return (reply["start_frame"], reply["end_frame"])
        else:
            return None

    def set_range(self, start_frame, end_frame):
        """
        Set the current range of the (primary) active timeline.

        :param start_frame: Requested range start frame number.
        :param end_frame: Requested range end frame number.
        :return: Tuple containing the range of the (primary) active timeline. None on error.
        """
        cmd = {
            "cmd": "set_range",
            "start_frame": start_frame,
            "end_frame": end_frame
        }

        reply = self.send(cmd)
        if self.is_valid_reply(reply):
            return (reply["start_frame"], reply["end_frame"])
        else:
            return None

    def get_default_timeline(self):
        """
        Get the project default timeline.

        Imported files (sources) are automatically added to this timeline.

        :return: Dictionary representing the timeline object (may be empty if unassigned). None on error.
        """
        cmd = {
            "cmd": "get_default_timeline"
        }

        reply = self.send(cmd)
        if self.is_valid_reply(reply):
            return reply["timeline"]
        else:
            return None

    def set_default_timeline(self, id):
        """
        Set the project default timeline. An empty 'id' string will result unassign the default timeline.

        Imported files (sources) are automatically added to this timeline.

        :return: Dictionary representing the timeline object (may be empty if unassigned). None on error.
        """
        cmd = {
            "cmd": "set_default_timeline",
            "id": id
        }

        reply = self.send(cmd)
        if self.is_valid_reply(reply):
            return True
        else:
            return False

    def get_active_in_viewer(self, index):
        """
        Get the source/timeline assigned to a viewer.

        :param index: Viewer index. (0 - Viewer A, 1 - Viewer B)
        :return: Dictionary representing the timeline object (may be empty if unassigned). None on error.
        """
        cmd = {
            "cmd": "get_active_in_viewer",
            "index": index
        }

        reply = self.send(cmd)
        if self.is_valid_reply(reply):
            return reply["timeline"]
        else:
            return None

    def set_active_in_viewer(self, id, index):
        """
        Set the source/timeline assigned to a viewer.

        An empty 'id' string will unassign a timeline from the viewer.

        :param index: Viewer index. (0 - Viewer A, 1 - Viewer B)
        :return: Dictionary representing the timeline object (may be empty if unassigned). None on error.
        """
        cmd = {
            "cmd": "set_active_in_viewer",
            "id": id,
            "index": index
        }

        reply = self.send(cmd)
        if self.is_valid_reply(reply):
            return True
        else:
            return False

    def set_viewer_layout(self, layout="single"):
        """
        Set the viewer layout to single, split horizontal or split vertical.

        :param layout: Desired layout ("single", "horizontal" or "vertical")
        :return: True on success. False otherwise.
        """
        cmd = {
            "cmd": "set_viewer_layout",
            "layout": layout,
        }

        reply = self.send(cmd)
        if self.is_valid_reply(reply):
            return True
        else:
            return False


if __name__ == "__main__":

    kpro = KeyframeProClient()
    if kpro.connect():
        print("Connected successfully.")
