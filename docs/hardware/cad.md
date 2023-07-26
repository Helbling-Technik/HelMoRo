# CAD 

## Downloads

In addition to the [Fusion 360 Widget](https://helbling1.autodesk360.com/g/shares/SHd38bfQT1fb47330c99885750fe7d15459b), we provide the model in the following formats:

- [Solidworks 2021](https://github.com/Helbling-Technik/HelMoRo/tree/5-upload-and-order-cad-files/cad/solidworks) 
- [STEP](https://github.com/Helbling-Technik/HelMoRo/tree/5-upload-and-order-cad-files/cad/step) 
- [STL](https://github.com/Helbling-Technik/HelMoRo/tree/5-upload-and-order-cad-files/cad/stl) 

Some files extend the file limit of 100 Mb, and therefore, we use [GitHub LFS](https://git-lfs.com/) (Large File Storage) to manage these large files effectively. Instructions how to use GitHub LFS can be found under [Collaboration](../../collaboration#accessing-the-repository).


## Naming Convention

The part number is of the following form:

**HEL-XX-UUYYY-RR**

- **HEL** is short for Helbling as it is an internal project.
- **XX** is the type, 01 is the main assembly, 03 is a sub-assembly, 04 is a generative part or sheet metal, 06 is a purchased electronic part.
- **UUYYY** is composed by **UU** which is user name (currently user 01, 02, 03 and 04 exist); **YYY** is the part number which can start from 000 then 001 etc..
- **RR** is revision number starting from 00 then 01 etc..


Additional comments:

- The part number YYY restarts from 000 for different part types or different users XX (for example: HEL-04-01000-00 and HEL-06-01000-00 can co-exist) .
- Fasteners that are usually normed parts such as screws and nuts have no part number.