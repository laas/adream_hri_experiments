# adream_hri_experiments
This package provides and record launch files, parameters, 3D models and other tools to run HRI experiments in the Adream environment, with the LAAS' RIS/HRI team tools.

## CONFIGURE

The package needs to create symlinks to external files located in the move3d/assets ([see move3d doc](https://www.openrobots.org/wiki/move3d#P3D_Files)). They contain the robot and object descriptions used by move3d.

These links are created when building the package (so when you call `catkin_make`), and will link to the directories `ADREAM/MACROS` and `urdf/COLLADA` in `$ROBOTPKG_BASE/share/move3d/assets`. That default base path can be changed using the ASSETS_DIR parameter. But it would be easier to run `initialize_links.sh /your/path/to/assets`. If you want to reset the links, you need to remove the file `p3d/.links_created`.

## Scope

Contributions are welcome by RIS/HRI members and associates. Keep in mind that contributions **must stay of generic use**, i.e. anyone else migth need this to use in their own experiments. It is not the place for any specific experiment setting (you were thinking in putting your `icraDemo2018.launch` here? Nope!)
