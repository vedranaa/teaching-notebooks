*This is a collection of notebooks useful for porosity analysis*

Porosity analysis covered here operates on binarized volume, whith the material and the pores separted. Binarization (segmentation) will influence the result of porosity analysis.

We cover two approaches:
* The approach based on **connected component analysis** (CC). This approach can give the number of pores, and the statistics related to each pore. The approach requires that the pores can be individually segmented. It is not suitable for analysis of larger connected regions.  
* The approach based on **local thicknes** (LT). This approach can be used when individual pores are difficult to separate, or for analysing larger regions. Downside is that we get no information about the number of pores.  

Reading material:
* [Note on porosity](http://people.compute.dtu.dk/vand/notes/porosity_course_note.pdf) is a course note for PhD course on porosity analysis. Note coveres connected component analysis. In that course we used matlab, but the processing is the same. The note covers segmentation and connected components. 
* [Article about local thickness](https://github.com/vedranaa/local-thickness/blob/main/Fast_local_thickness.pdf), published at Workshop on Computer Vision for Microscopy Image Analysis (CVMI) held in conjunction with the CVPR 2023 conference.
* Optional: [Note on visualization using paraview](http://people.compute.dtu.dk/vand/notes/ParaView_notes.pdf).

* Connected component analysis [wikipedia link](https://en.wikipedia.org/wiki/Connected-component_labeling).
* Lognormal distribution [wikipedia link](https://en.wikipedia.org/wiki/Log-normal_distribution)



## Cement analysis notebooks
Cement data is very suitable for porosity analysis. If you look carefuly, you will see that cement used here contains two types of porositiesy. These are air bobbles and polymer spheres. The analysis below ignores this and simply binarizes the volume. Cement data is downloaded from the notebooks, and can also be  downloaded [here](https://qim.compute.dtu.dk/data-repository/cement_data.zip). 

-[02509 cement porosity analysis](https://github.com/vedranaa/teaching-notebooks/blob/main/02509_cement_porosity.ipynb), segmentation and CC-based porosity analysis and quantification.

-[Cement porosity analysis](https://github.com/vedranaa/teaching-notebooks/blob/main/Cement_porosity_analysis.ipynb), comparison of CC-based porosity analysis and LT-based porosity analysis.

-[02510 guantification example](https://github.com/vedranaa/teaching-notebooks/blob/main/02510_quantification_material_fraction.ipynb), and example of collecting measures in smaller subvolumes of the larger volume. Here we collect material fraction, so a very simple measurement. This is a part of code provided in 02510 course.

-[02510 quantification pore thickness](https://github.com/vedranaa/teaching-notebooks/blob/main/02510_quantification_pore_thickness.ipynb) local thickness on a subvolume for quantification of material properties. This is a part of code provided in 02510 course.

-[02510 quantification](https://github.com/vedranaa/teaching-notebooks/blob/main/02510_quantification.ipynb) block-wise quantification of material properties using local thickness. This is a solution of the task given in 02510 course.





## Hourglass analysis notebooks
Hourglas data depicts the sand grains in a hourglas. Data can be downloaded from [hourglass page](https://qim.compute.dtu.dk/data-repository/pages/hourglass.html) of QIM data repository..

- [02509_hourglass cropping](https://github.com/vedranaa/teaching-notebooks/blob/main/02509_hourglass_cropping.ipynb) preprocessing the data after being downloaded.

- [02509 hourglass segmentation](https://github.com/vedranaa/teaching-notebooks/blob/main/02509_hourglass_segmentation.ipynb) ([colab link](https://colab.research.google.com/github/vedranaa/teaching-notebooks/blob/main/02509_hourglass_segmentation.ipynb)) segmentation used both for CC porosity analysis and LT porosity analysis.

- [02509 hourglass connected components](https://github.com/vedranaa/teaching-notebooks/blob/main/02509_hourglass_connected_components.ipynb) ([colab link](https://colab.research.google.com/github/vedranaa/teaching-notebooks/blob/main/02509_hourglass_connected_components.ipynb)) CC porosity analysis and quantification.

- [02509 hourglass local thickness](https://github.com/vedranaa/teaching-notebooks/blob/main/02509_hourglass_local_thickness.ipynb) ([colab link](https://colab.research.google.com/github/vedranaa/teaching-notebooks/blob/main/02509_hourglass_local_thickness.ipynb)) LT porosity analysis and quantification.
You can also check other notebooks in [local thicknes repository](https://github.com/vedranaa/local-thickness), including [examples](https://github.com/vedranaa/local-thickness/blob/main/Examples.ipynb) or [demos](https://github.com/vedranaa/local-thickness/blob/main/Demos.ipynb). Colab links: [examples](https://colab.research.google.com/github/vedranaa/local-thickness/blob/main/Examples.ipynb) or [demos](https://colab.research.google.com/github/vedranaa/local-thickness/blob/main/Demos.ipynb).


## Additional material on 2D and 3D image analysis

The repository [https://github.com/vedranaa/teaching-notebooks](https://github.com/vedranaa/teaching-notebooks) contains various notebooks used for teaching. You may find other notebooks usefull. 



