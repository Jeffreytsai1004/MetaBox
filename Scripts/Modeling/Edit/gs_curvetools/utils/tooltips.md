<!-- 
Tooltips are added in format:
    # Widget
    Tooltip
-->

<!-- main.py -->

<!-- Options Menu -->
# importCurves
Imports Curves that were Exported using the Export Button.
NOTE: Only import files that were exported using Export Curves button.
WARNING: This operation is NOT undoable!

# exportCurves
Exports selected curves into a .curves (or .ma) file. Can then be Imported using Import Curves.

# changeScaleFactor
Opens a window that controls the Scale Factor.
Scale factor determines the initial scale of the created curve and adjusts other parameters.
Scale factor is stored in a global preset, in the scene and on each curve.
Priority of scale factors Curve>Scene>Global.
NOTE: Using the correct scale factor can help with the control of the curves and helps in avoiding bugs due to very large or very small scenes.

# globalCurveThickness
Opens a window that controls the thickness of the curves in the scene as well as the global curve thickness preset across the scenes.

# setAOSettings
Manually sets the recommended AO settings for older Maya versions.
These AO settings are needed to use the "See Through" or "Toggle Always on Top" functions.
Are applied automatically by those functions.

# setTransparencySettings
Sets recommended transparency settings for Maya viewport.
***
Simple Transparency is fast but very inaccurate render mode. Only suitable for simple, one layer hair.
Object Sorting Transparency has average performance impact and quality. Can have issues on complex multi-layered grooms.
Depth Transparency - these are the optimal settings for the highest quality of the hair cards preview. Can have performance impact on slower systems.

# convertToWarpCard
Converts selection to Warp Cards.
Compatible attributes are retained.

# convertToWarpTube
Converts selection to Warp Tubes.
Compatible attributes are retained.

# convertToExtrudeCard
Converts selection to Extrude Cards.
Compatible attributes are retained.

# convertToExtrudeTube
Converts selection to Extrude Tubes.
Compatible attributes are retained.

# syncCurveColor
Toggles the syncing of the curve color to the layer color.

# colorizedRegroup
Toggles the colorization of the regrouped layers when Regroup by Layer function is used.

# colorOnlyDiffuse
Colorize only the diffuse component of the card material.
Alpha will stay the same.

# checkerPattern
Toggles the use of the checker pattern when the Color mode is enabled.

# ignoreLastLayer
Toggles the filtering (All, Curve, Geo) and Extraction (Extract All) of the last layer. If enabled, the last layer is ignored.
NOTE: Last layer is typically used for templates, so it is ignored by default.

# ignoreTemplateCollections
Ignores the filtering (All, Curve, Geo) and Extraction (Extract All) of all the collections that have "template" in their name. Case insensitive.

# groupTemplateCollections
Collections that have "template" in their name (case insensitive) will be grouped together into "CT_Templates" group by Regroup By Layer function.

# syncOutlinerLayerVis
Syncs the outliner and layer visibility. If enabled, hiding the layer will also hide the curve groups in the outliner.

# keepCurveAttributes
If enabled, the attributes that are stored in the curve will be restored if the curve that was duplicated (on its own, without the geo) is used to create other cards or tubes.
If disabled, the attributes will be ignored and reset.
Example:
1. Create a card and change its twist value.
2. Ctrl+D and Shift+P the curve (not the curve group).
3. Click Curve Card and the twist value will be restored on a newly created card.

# boundCurvesFollowParent
Will ensure that moving a parent curve in a Bound Object (Bound Group) will also move all the child curves along with it to a new layer. Recommended to keep this enabled.

# massBindOption
Will bind selected hair clump (or geometry) to all selected "empty" curves.

# bindDuplicatesCurves
Will automatically duplicate the curves before binding them to the curve, leaving old curves behind with no edits.

# bindFlipUVs
Enabling this option will flip the UVs of the original cards before binding them to the curve.
It will also automatically flip the bound geo and rotate it 90 deg.
This option will also flip the UVs back when using Unbind for better workflow.
Disabling this option will result in an old Bind/Unbind behaviour.

# populateBlendAttributes
Enables blending of the attributes when using Add Cards/Tubes or Fill functions.

# convertInstances
Will automatically convert instanced curves to normal curves before any other function is applied.

# replacingCurveLayerSelection
Will disable additive selection for the layers. When holding Ctrl and clicking on a new layer, old layer will be deselected automatically.

# useAutoRefineOnNewCurves
Automatically enables auto-refine on the new curves.

# flipUVsAfterMirror
Enabling this option will flip the UVs horizontally after mirroring the cards to achieve exact mirroring.

# enableTooltips
Will toggle the visibility of these tooltips you are reading right now.

# showLayerCollectionsMenu
Shows layer collections menu widget.

# importIntoANewCollection
If enabled, all the imported curves will be placed into a new "Imported Curves" layer collection.
If disabled, all the imported curves will be placed into the "Main" layer collection

# layerNumbersOnly
Layers will use only numbers if enabled.

# convertToNewLayerSystem
Converts all the layers in the scene to a new layer system that is hidden from the Channel Box Display Layers window.
Layers can still be accessed from Window->Relationship Editors->Display Layer window.

# updateLayers
Utility function that will manually update all layers. Used for if layers are correct for some reason.

# resetToDefaults
Resets every option and the GS CurveTools to the default "factory" state.

# maya2020UVFix
This function will fix any broken UVs when trying to open old scenes in Maya 2020 or 2022 or when opening scenes in 2020 and 2022 when using Maya Binary file type. This will have no effect on older versions of Maya (<2020). This bug is native to Maya and thus can’t be fixed in GS CurveTools plug-in.

# mayaFixBrokenGraphs
This function will attempt to fix all the broken graphs in the scene.
Use if one of the graphs (Width, Twist or Profile) is in a broken state.

# convertBezierToNurbs
Converts the selected Bezier curves to NURBS curves.
Bezier curves are not supported by the GS CurveTools.

# maya2020TwistAttribute
This function will fix any broken cards created in Maya 2020.4 before v1.2.2 update.

# maya2020UnbindFix
This function will fix any cards that are not unbinding properly and were created before v1.2.3 update in Maya 2020.4.

# deleteAllAnimationKeys
This function will delete all the animation keys on all the curves present in the scene.
This can fix deformation issues when using duplicate or other GS CurveTools functions.
Some functions (like duplicate) will delete the keys automatically, however the keys can still cause issues.

<!-- Main Buttons -->

# warpSwitch
Advanced cards and tubes suitable for longer hair. 
Additional options and controls. 
Slower than Extrude (viewport performance). 
Can have issues on very small scales.

# extrudeSwitch
Simple cards and tubes suitable for shorter hair and brows.
Has limited controls.
Much faster than Warp (viewport performance).
Better for small scales.

# newCard
Creates a new Card in the middle of the world. Used at the beginning of the project to create templates.

# newTube
Creates a new Tube in the middle of the world. Used at the beginning of the project to create templates.

# curveCard
Converts selected Maya curve to CurveTools Card.

# curveTube
Converts selected Maya curve to CurveTools Tube.

# gsBind
Binds selection to a single curve. Creates a Bind Group. Selection options:
1. Single "empty" curve (default Maya curve) and single combined geometry.
2. Single "empty" curve (default Maya curve) and any number of Curve Cards and Curve Tubes.
***
Shift + Click will duplicate the original curves/geo before binding it to the empty curve.
Same option is available in the Options menu (Duplicate Curves Before Bind).

# gsUnbind
UnBinds geometry or Cards/Tubes from selected Bound object.
Geometry and Cards/Tubes will be placed at the origin.

# addCards
Creates Cards in-between selected Cards based on the Add slider value.
Bound objects are NOT supported.
NOTE: Selection order defines the direction of added Cards if more than 2 initial Cards are selected.

# addTubes
Creates Tubes in-between selected Tubes based on the Add slider value.
Bound objects are NOT supported.
NOTE: Selection order defines the direction of added Tubes if more than 2 initial Tubes are selected.

# gsFill
Creates Cards/Tubes or Bound Groups in between selected Cards/Tubes or Bound Groups based on the Add slider value.
NOTE 1: Selection order defines the direction of added curves if more than 2 initial curves are selected.
NOTE 2: The type of Card or Tube or Bound Group is defined by the previous curve in the selection chain.

# gsSubdivide
Subdivides selected curve into multiple curves based on the Add slider value
Shift + Click subdivides selected curve but does not delete the original curve

# gsEdgeToCurve
Converts selected geometry edges to curves.
Multiple unconnected edge groups can be selected at the same time.

# gsCardToCurve
Opens the Card-to-Curve UI
Card to curve algorithm will attempt to generate CurveTools cards from selected geometry cards.
Selected geometry cards should be one sided meshes.
Selected geometry cards should be separate objects.

# layerCollectionsComboBox
Layer collections drop-down menu.
Allows to separate the project into different layer collections, up to 80 layers in each collection.
Has additional functionality in markdown menu (Hold RMB):
***
Markdown menu:
1. Clear - will delete all the cards from the current layer. Undoable operation.
2. Merge Up, Merge Down - merge all the cards from the current layer to the layer above or below it.
3. Copy, Paste - will copy all the cards from the current layer and paste them to the layer that user selects.
4. Move Up, Move Down - will rearrange the current layer collections by moving the currently selected collection up or down in the list.
5. Rename - will rename the current layer collection

# layerCollectionsPlus
Add additional layer collection after the current one.

# layerCollectionsMinus
Remove current layer collection. All the cards from the removed collection will be merged one layer UP.

# gsAllFilter
Layer filter. Controls the visibility of all objects in all layers:
Normal click will show all curves and geometry in all layers.
Shift + Click will hide all curves and geometry in all layers
Ctrl + Click will show all the curves and geometry in all layers and all collections.
Ctrl + Shift + Click will hide all curves and geometry in all layers and all collections.

# gsCurveFilter
Layer filter. Hides all geometry and shows all the curves in all layers.
Ctrl + Click will do the same thing, but for all layers and all collections.
NOTE: Holding RMB will open a marking menu with Toggle Always on Top function as well as "Auto-Hide Inactive Curves" function.
Toggle Always on Top function will toggle the Always on Top feature that will show the curve component always on top. The effect is different in different Maya versions
Auto-Hide Inactive Curves will hide all the curve components on all inactive layer collections when switching between collections.

# gsGeoFilter
Layer filter. Hides all curves and shows only geometry.
Ctrl + Click will do the same thing, but for all layers and all collections.

# colorMode
Color mode toggle. Enables colors for each layer and (optionally) UV checker material.
NOTE: Checker pattern can be disabled in the Options menu

# curveGrp0
Curve Layers that are used for organization of the cards and tubes in the scene.
Selected layer (white outline) will be used to store newly created cards.
Holding RMB will open a marking menu with all the functions of current layer.
***
Key Combinations:
Shift + Click: additively select the contents of the layers.
Ctrl + Click: exclusively select the contents of the layer.
Alt + Click: show/hide selected layer.
Ctrl + Shift: show/hide curve component on selected layer.
Ctrl + Alt: show/hide geo component for the selected layer.
Shift + Alt + Click: isolate select the layer.
Shift + Ctrl + Alt + Click: enable Always on Top for each layer (only for Maya 2022+).
***
Layer MMB Dragging:
MMB + Drag: move the contents of one layer to another layer. Combine if target layer has contents.
MMB + Shift + Drag: copy the contents of one layer to another layer. Copy and Add if target layer has contents.

# gsExtractSelected
Extracts (Duplicates) the geometry component from the selected curves:
***
Key Combinations:
Normal click will extract geometry and combine it.
Shift + Click will extract geometry as individual cards.
Ctrl + Click will extract geometry, combine it, open export menu and delete the extracted geo after export.
Shift + Ctrl click will extract geometry, open export menu and delete the extracted geo after export.

# gsExtractAll
Extracts (Duplicates) the geometry component from all layers and collections. Original layers are HIDDEN, NOT deleted:
Last Layer in the current Collection is ignored by default. Can be changed in the options.
Collections with "template" in their name (case insensitive) will be ignored by default. Can be changed in the options.
***
Key Combinations:
Normal click will extract geometry and combine it.
Shift + Click will extract geometry as individual cards grouped by layers.
Ctrl + Click will extract geometry, combine it, open export menu and delete the extracted geo after export.
Shift + Ctrl click will extract geometry, open export menu and delete the extracted geo after export.

# gsSelectCurve
Selects the curve components of the selected Curve Cards/Tubes.
NOTE: Useful during the selection in the outliner.

# gsSelectGeo
Selects the geometry component of the selected Curve Cards/Tubes.
NOTE: Useful for quick assignment of the materials.

# gsSelectGroup
Selects the group component of the selected Curve Cards/Tubes.
NOTE: Useful when you are deleting curves from viewport selection.

# gsGroupCurves
Groups the selected curves and assigns the name from Group Name input field (or default name if empty).

# gsRegroupByLayer
Regroups all the curves based on their layer number, group names and collection names.
Group names can be changed in the Layer Names & Colors menu.
Groups can be colorized if the "Colorize Regrouped Layers" is enabled in the Options menu.
Collections with "template" in their name will be grouped under "CT_Templates". Can be changed in the options.

# gsGroupNameTextField
The name used by the Group Curves function.
If empty, uses the default name.

# gsCustomLayerNamesAndColors
Opens a menu where group names and colors can be changed and stored in a global preset.

# gsTransferAttributes
Transfers attributes from the FIRST selected curve to ALL the other curves in the selection.
NOTE: Shift + Click transfers the attributes from the LAST selected curve to ALL others.
NOTE2: Holding RMB on this button opens a marking menu with Copy-Paste and Filter functionality

# gsTransferUVs
Transfers UVs from the FIRST selected curve to ALL the other curves in the selection.
NOTE: Shift + Click transfers the UVs from the LAST selected curve to ALL others.
NOTE2: Holding RMB on this button opens a marking menu with Copy-Paste and Filter functionality

# gsResetPivot
Resets the pivot on all selected curves to the default position (root CV).

# gsRebuildWithCurrentValue
Rebuild selected curves using current rebuild slider value

# gsResetRebuildSliderRange
Reset rebuild slider range (1 to 50)

# gsDuplicateCurve
Duplicates all the selected curves and selects them. 
NOTE: You can select either NURBS curve component, geometry component or group to duplicate.

# gsRandomizeCurve
Opens a window where different attributes of the selected curves can be randomized:
1. Enable the sections of interest and change the parameters.
2. Dragging the sliders in each section enables a PREVIEW of the randomization. Releasing the slider will reset the curves.
3. Click Randomize if you wish to apply the current randomization.

# gsExtendCurve
Lengthens a selected curves based on the Factor slider.

# gsReduceCurve
Shortens the selected curves based on the Factor slider.

# gsSmooth
Smoothes selected curves or curve CVs based on the Factor slider.
NOTE 1: At least 3 CVs should be selected for component smoothing.
NOTE 2: Holding RMB will open a marking menu where you can select a stronger smoothing algorithm.

# mirrorX
Mirrors or Flips all the selected curves on the World X axis.

# mirrorY
Mirrors or Flips all the selected curves on the World Y axis.

# mirrorZ
Mirrors or Flips all the selected curves on the World Z axis.

# gsControlCurve
Adds a Control Curve Deformer to the selected curves. Can be used to adjust groups of curves.
NOTE 1: Should NOT be used to permanently control clumps of cards. Use Bind instead.

# gsApplyControlCurve
Applies the Control Curve Deformer.
Either the Control Curve or any controlled Curves can be selected for this to work.

# gsCurveControlWindow
Opens a Curve Control Window. Contains all the available controls for curves.

# gsUVEditorMain
Opens a UV editor that can be used to setup and adjust UVs on multiple cards.
NOTE 1: Lambert material with PNG, JPG/JPEG or TIF/TIFF (LZW or No Compression) texture file is recommended. TGA (24bit and no RLE) is also supported.
NOTE 2: Make sure to select the curves or the group, not the geo, to adjust the UVs.
NOTE 3: Using default Maya UV editor will break GS CurveTools Cards, Tubes and Bound Groups.
NOTE 4: Default UV editor can be used when custom geometry is used in a Bound Groups.

<!-- ui.py --->
<!-- Curve Control Window Buttons and Frames --->

# gsLayerSelector
Shows the Layer of the selected curve.
Selecting different layer will change the layer of all the selected curves.

# gsColorPicker
Layer/Card Color Picker.

# gsCurveColorPicker
Curve Color Picker.

# selectedObjectName
Selected object name. Editing this field will rename all the selected objects.

# lineWidth
Controls the thickness of the selected curves.

# gsBindAxisAuto
Automatic selection of the bind Axis (recommended).
NOTE: Change to manual X, Y, Z axis if bind operation result is not acceptable.

# AxisFlip
Flips the direction of the bound geometry.

# editOrigObj
Temporarily disables curve bind and shows the original objects.
Used to adjust the objects after the bind.
To add or remove from the Bound group use Unbind.

# selectOriginalCurves
Selects the original curves that were attached to a bind curve.
Allows to edit their attributes without using Unbind or Edit Original Objects

# twistCurveFrame
Advanced twist control graph. Allows for precise twisting of the geometry along the curve. Click to expand.

# Magnitude
Twist multiplier. The larger the values, the more the twist. Default is 0.5.

# gsTwistGraphResetButton
Resets the graph to the default state.

# gsTwistGraphPopOut
Opens a larger graph in a separate window that is synced to the main graph.

# widthLockSwitch
Links/Unlinks the X and Z width sliders.
If linked, the sliders will move as one.

# LengthLock
Locks/Unlocks the length slider.
When Locked the geometry is stretched to the length of the curve and the slider is ignored.

# widthCurveFrame
Advanced width control graph. Allows for precise scaling of the geometry along the curve. Click to expand.

# gsWidthGraphResetButton
Resets the graph to the default state.

# gsWidthGraphPopOut
Opens a larger graph in a separate window that is synced to the main graph.

# profileCurveGraph
Advanced control over the profile of the card. Modifies the profile applied by the Profile slider. Click to expand.
Add or remove points and change them to increase or decrease the Profile value along the curve.

# autoEqualizeSwitchOn
Locks the points horizontally to equal intervals to avoid geometry deformation.

# autoEqualizeSwitchOff
Unlocks the points and allows for the full control.

# equalizeCurveButton
Snaps the points to the equal horizontal intervals.

# gsResetProfileGraphButton
Resets the curve to the default state.

# gsProfileGraphPopOut
Opens a larger graph in a separate window that is synced to the main graph.

# reverseNormals
Reverses the normals on the selected cards/tubes.

# orientToNormalsFrame
Orient selected cards/tubes to the normals of the selected geo.

# gsOrientToNormalsSelectTarget
Set selected mesh as a target for the algorithm.

# orientRefreshViewport
Toggles the viewport update during the alignment process.
Disabling can speed up the process.

# gsOrientToNormals
Starts the alignment process. 
Will align the selected cards to the normals of the selected geometry.

# flipUV
Flips the UVs of the card/tube horizontally.

# resetControlSliders
Resets the range of the sliders to the default state.

# UVFrame
Legacy controls for the UVs. Just use the new UV Editor.

# solidifyFrame
Expands controls that control the thickness of the cards/tubes.

# solidify
Toggles the thickness of the geometry.

<!-- Curve Control Window Sliders --->

# lengthDivisions
Change the length divisions of the selected cards/tubes.

# dynamicDivisions
Toggles the dynamic divisions mode.
Dynamic divisions will change the divisions of the cards/tubes based on the length of the curves.
In dynamic divisions mode, L-Div slider will control the density of the divisions, not the fixed divisions count.

# widthDivisions
Change the width divisions of the selected cards/tubes.

# Orientation
Change the orientation of the card/tube around the curve.

# Twist
Smoothly twist the entire geometry card/tube. Twists the tip of the card.

# invTwist
Smoothly twist the entire geometry card. Twists the root of the card.

# Width
Change the width of the selected card.

# Taper
Linearly changes the width of the card/tube along the length of the curve.

# WidthX
Change the width of the tube along the X axis.

# WidthZ
Change the width of the tube along the Z axis.

# Length
Change the length of the attached geometry. Works only when Length Unlock button is checked.

# Offset
Offset the geometry along the curve.

# Profile
Change the profile of the card along the length of the curve uniformly.

# profileSmoothing
Smoothing will smooth the profile transition.

# otherFrame
Other less used options

# curveRefine
Controls the number of "virtual" vertices on the curve. These are the vertices that are used to calculate the geometry deformation.
Zero (0) value will disable the refinement and the geometry will be attached directly to the curve. The fastest option.
Larger refine values means smoother geometry that is a closer fit to the curve.
Only increase past 20 if you need additional precision or if there are any visual glitches with the geometry.
Large refine values can cause significant performance drop, lag and other issues on smaller curve sizes.
Recommended values are: 
20 for curves with less than 20 CVs.
0 (disabled) or same as the number of CVs for curves with more than 20 CVs.

# autoRefine
Enables auto-refine for selected curves. Recommended to keep this on.
Manual refinement can be helpful if the geometry deformation is wrong or not precise enough.

# samplingAccuracy
Increases the sampling accuracy of the deformer that attaches the geometry to a curve.
Larger values = more precise geometry fit to a curve and more lag.

# curveSmooth
Smoothing of the geometry that is attached to a curve.

# surfaceNormals
Changes the smoothing angle of the normals of the geometry.

# gsIterationsSlider
Controls the number of iterations per card.

# gsMinimumAngle
Controls the target angle difference between the normal of the mesh and the card.

# solidifyThickness
Controls the amount of thickness on the geometry.

# solidifyDivisions
Controls the number of divisions on the solidify extrusion.

# solidifyScaleX
Changes the scale on the X axis.

# solidifyScaleY
Changes the scale on the Y axis.

# solidifyOffset
Controls the offset of the solidify extrusion.

# solidifyNormals
Controls the smoothing angle for normals of the solidify extrusion.

# geometryHighlight 
If enabled, selecting the curve will also highlight the geometry component that is attached to that curve.
Works only on GS CurveTools curves and geo.

# curveHighlight
If enabled, selected curves and their components will be additinally highlighted for better visibility.
The curves and components will be in X-Ray mode by default.
Colors and transparency values can be changes in the menu below.

# gsSelectedCVColor
Selected CV highlight color

# gsSelectedCVAlpha
Selected CV highlight transparency (alpha)

# gsDeselectedCVColor
Deselected CV highlight color

# gsDeselectedCVAlpha
Deselected CV highlight transparency (alpha)

# curveVisibility
Toggle selected curves highlight

# gsCurveHighlightColor
Selected curve highlight color

# gsCurveHighlightAlpha
Selected curve highlight transparency (alpha)

# hullVisibility
Toggle hull visibility.
Hull is a line that connects all the CVs on the curve.

# gsHullHighlightColor
Hull highlight color

# gsHullHighlightAlpha
Hull highlight transparency (alpha)

# advancedVisibilityFrame
Better highlights for selected curves and components.

# lazyUpdate
Enables lazy update for selected curves.
Lazy update can slightly increase the performance of the highlight,
however it has some visual drawbacks (curve highlight can fail to update when switching curves in component selection mode)

# alwaysOnTop
Toggles X-Ray (always on top) drawing for highlighted components.
Disabling this defeats the purpose of the advanced visibility, but hey, it's your choice.

# curveDistanceColor
Toggles the distance color effect on the curve highlight.
Distance color darkens the curve color the further it is from the camera.

# cvDistanceColor
Toggles the distance color effect on the CV highlight.
Distance color darkens the CVs color the further it is from the camera.

# hullDistanceColor
Toggles the distance color effect on the hull highlight.
Distance color darkens the hull color the further it is from the camera.

# gsDistanceColorMinValue
Distance color minimum.
This value is the minimum allowed color multiplier for the Distance Color effect.
The lower this value, the darker further parts of the curve will be.
Black at 0.0
Original color at 1.0

# gsDistanceColorMaxValue
Distance color maximum.
This value is the maximum allowed color multiplier for the Distance Color effect.
The higher this value, the brighter closest parts of the curve will be.
Black at 0.0
Original color at 1.0

# CVocclusion
Toggles the experimental CV occlusion mode (hull is affected as well)
When the appropriate mesh name is added to Occluder Mesh input field,
this function will automatically hide CVs and hull lines that are behind this mesh (even in X-Ray mode).
Warning: enabling this mode can negatively impart viewport performance.

# gsSelectOccluderButton
This button adds the selected mesh name to the Occluder Mesh input field.

# gsOccluderMeshName
Type the full path for the occluder mesh here, or use the "Select Occluder" button on the left <-


<!-- Layer Customization --->

# gsGenerateLayerColorGradient
Generate a color gradient for the layer colors.
Rows control the number of Rows to generate.
Left color picker sets the initial color.
Right color picker sets the final color.

# gsRandomizeLayerColors
Generate random colors for the layers.
SatMin controls the minimum allowed saturation.
SatMax controls the maximum allowed saturation.

# gsResetAllLayerColors
Resets all the color swatches to the default color.

# gsGetCurrentSceneLayers
Populates the menu with the names and colors stored in the scene.

# gsSetAsCurrentSceneLayers
Applies the names and colors from the menu to the scene.

# gsLoadGlobalLayerPreset
Load the global names and colors preset to the menu.
NOTE: Don't forget to Set to Scene before closing the menu.

# gsSaveGlobalLayerPreset
Saves the current names and colors from the menu to the global preset.

<!-- UV Editor Window --->

# gsUVSelect
Enables the selection of the UVs.
Drag to draw a box selection.

# gsUVMove
Enables the Move tool.
Move the selected UVs or move individual UVs if nothing is selected.

# gsUVRotate
Enables the Rotation of the selected UVs.
Hold LMB and drag anywhere in the viewport to rotate the selected UVs.
Rotation pivot is the center of the individual unscaled UV.

# gsUVScale
Enables the Scaling of the selected UVs. 
Hold LMB and drag in the viewport to scale the card Horizontally of Vertically.
Repeated hotkey click will toggle between Horizontal and Vertical scaling.

# gsUVHorizontalScale
Horizontal scaling mode selector.

# gsUVVerticalScale
Vertical scaling mode selector.

# gsDrawUVs
Enables the UVs Drawing Tool:
1. Select UVs using Selection Mode.
2. Enable the UV Drawing Tool.
3. Draw a UV Rectangle anywhere in the viewport to create/move the UVs there.

# gsHorizontalFlipUV
Flips the selected UVs horizontally.
Flipped UVs have the blue circle indicator inside the root rectangle.

# gsVerticalFlipUV
Flips the selected UVs vertically.
 
# gsResetUVs
Resets the selected UVs to the default 0,1 rectangle.

# gsSyncSelectionUVs
Syncs selection between UV editor and Maya Viewport.

# gsRandomizeUVs
Randomize selected UV positions between already existing UV positions.
***
Normal click will keep the overall density distribution of the UVs.
This means that if there is one card in one position and twenty cards in the other,
it will keep this distribution of 1 to 20.
***
Shift+Click will ignore the original density distribution
and simply randomize the UVs between the original positions.

# gsFocusUVs
Focuses on the selected UVs or on all the UVs if nothing is selected.

# gsUVIsolateSelect
Hides all the unselected UVs and shows only the selected ones.

# gsUVShowAll
Shows all the hidden UVs.

# UVEditorUseTransforms
Use "Coverage" and "Translate Frame" parameters from place2dTexture node for texture.
Offset is not supported.
Diffuse and Alpha channel MUST have the same coverage and translate frame values.

# UVEditorTransparencyToggle
Enable texture map transparency using Alpha map from Transparency plug in the material node

# UVEditorBGColorPicker
Background Color

# UVEditorGridColorPicker
Grid Color

# UVEditorFrameColorPicker
Frame Color

# UVEditorUVFrameSelectedColorPicker
Selected UV frame color

# UVEditorUVFrameDeselectedColorPicker
Deselected UV frame color

# UVEditorUVCardFillColorPicker
UV frame background color

<!-- Card to Curve Window --->

# gsCardToCurve_outputTypeSwitch
Controls the output of Card-to-Curve algorithm

# gsCardToCurve_generateCards
Generate cards from selected one-sided geometry

# gsCardToCurve_generateCurves
Generate curves from selected one-sided geometry

# gsCardToCurve_cardType
Controls the type of generated cards

# gsCardToCurve_warp
Generate Warp cards

# gsCardToCurve_extrude
Generate Extrude cards

# gsCardToCurve_matchAttributes
Controls which attributes on the new cards should be approximated from the original geometry.
NOTE: This process is not perfect and final result can be inaccurate.

# gsCardToCurve_orientation
Match orientation attribute during the generation process

# gsCardToCurve_width
Match orientation attribute during the generation process

# gsCardToCurve_taper
Match taper attribute during the generation process

# gsCardToCurve_twist
Match twist attribute during the generation process

# gsCardToCurve_profile
Match profile attribute during the generation process

# gsCardToCurve_material
Copy material (shader) from the original geometry

# gsCardToCurve_UVs
Tries to approximate the UVs from the original geometry
NOTE: Matches the bounding box of the UVs. Rotated and deformed UVs are not matched precisely.

# gsCardToCurve_UVMatchOptions
Controls UV matching behaviour

# gsCardToCurve_verticalFlip
Vertically flip matched UVs

# gsCardToCurve_horizontalFlip
Horizontally flip matched UVs

# gsCardToCurve_reverseCurve
Reverse generated curve direction
Root CV should be generated near the scalp of the model.
Enable or disable if resulting card direction and taper are reversed.

# gsCardToCurve_convertSelected
Convert selected geometry to cards or curves based on the options
