var = ZomGet("Vars.AutoSelect.Mosaic.Developability")

ZomSet({Path="Prefs.FileSuffix", Value=""})
ZomSelect({PrimType="Edge", WorkingSet="Visible", Select=true, ResetBefore=true, ProtectMapName="Protect", FilterIslandVisible=true, Auto={QuasiDevelopable={Developability=var, IslandPolyNBMin=1, FitCones=false, Straighten=true}, HandleCutter=true, StoreCoordsUVW=true, FlatteningMode=0, FlatteningUnfoldParams={Iterations=1, BorderIntersections=true, TriangleFlips=true}}})
ZomCut({PrimType="Edge", WorkingSet="Visible"})
ZomLoad({Data={CoordsUVWInternalPath="Mesh.Tmp.AutoSelect.UVW"}})
ZomIslandGroups({Mode="DistributeInTilesByBBox", WorkingSet="Visible", MergingPolicy=8322})
ZomIslandGroups({Mode="DistributeInTilesEvenly", WorkingSet="Visible", MergingPolicy=8322, UseTileLocks=true, UseIslandLocks=true})
ZomPack({ProcessTileSelection=false, RecursionDepth=1, RootGroup="RootGroup", WorkingSet="Visible", Scaling={Mode=2}, Rotate={}, Translate=true, LayoutScalingMode=2})

