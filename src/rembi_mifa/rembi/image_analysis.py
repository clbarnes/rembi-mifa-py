from pydantic import BaseModel


class ImageAnalysis(BaseModel):
    analysis_overview: str
    """How image analysis was carried out.

    ## Examples
    - Image segmentation was performed for each 2D slice using a program called ilastik, which utilizes semantic segmentation. 3D object creation from 2D binary images and feature extraction was performed in a program called Arivis.

      Each 3D-SIM image contained one nucleus (in a small number of cases multiple nuclei were present, which did not affect the analysis). The image analysis pipeline contained six main steps: bivalent skeleton tracing, trace fluorescence intensity quantification, HEI10 peak detection, HEI10 foci identification, HEI10 foci intensity quantification, and total bivalent intensity quantification. Note that the normalization steps used for foci identification differ from those used for foci intensity quantification; the former was intended to robustly identify foci from noisy traces, whilst the latter was used to carefully quantify foci HEI10 levels.

      Images were deconvolved using the default conservative deconvolution method using DeltaVision Softworx software. Image quantification was carried out using Fiji (Schindelin et al, 2012). Deconvolved images were compressed to 2D images displaying the maximum intensity projection for each pixel across z-stacks listed in Table S7 (column “Projected”). Cell and nuclear areas were outlined using thresholding functions on the background TRITC signal and DAPI signal, respectively. Dots corresponding to transcripts were then counted for both nuclear and cytoplasmic areas for each image by applying the “Find Maxima” command with a noise tolerance specified in Table S7 (column “Maxima”). Bar charts show the mean number of dots per nuclear area and cytoplasmic area across all images for all combined replicates.
    """
