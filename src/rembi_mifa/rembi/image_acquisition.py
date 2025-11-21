from __future__ import annotations
from pydantic import BaseModel


class ImageAcquisition(BaseModel):
    imaging_method: ImagingMethod
    imaging_instrument: str
    """Description of the instrument used to capture the images.

    ## Examples
    - Zeiss Elyra PS1
    - Luxendo MuVi SPIM light-sheet microscope
    - DeltaVision OMX V3 Blaze system (GE Healthcare) equipped with a 60x/1.42 NA PlanApo oil immersion objective (Olympus), pco.edge 5.5 sCMOS cameras (PCO) and 405, 488, 593 and 640 nm lasers
    """

    image_acquisition_parameters: str
    """How the images were acquired, including instrument settings/parameters.

    ## Examples
    - Two and three days after surgery, sparse labeling of OPCs was achieved by i.p. injection of Tamoxifen (Tam; 180mg/kg bodyweight). Imaging fields of view containing identified OPCs were selected to obtain 10-20 SPOTs per mouse. Chronic 2-photon imaging was performed starting 3 days after surgery. All SPOTs were checked on a daily basis and no z-stack was acquired if no changes occurred. The imaging was performed on custom-built 2-photon microscope (Sutter Instrument Movable Objective Microscope type) using a long-working distance objective (water immersion, 16x magnification, 0.8NA, Nikon) and equipped with a ytterbium-doped laser system at 1045nm and 200fs (Femtotrain, High-Q lasers) or a fiber oscillator 45 laser at 1070nm (Fidelity-2, Coherent) to excite tdTomato labeled cells in the CC. Emission light was detected using a photomultiplier tube (Hamamatsu) after passing a red emission filter (610/75 nm; AHF).

      Embryos were imaged on a Luxendo MuVi SPIM light-sheet microscope, using 30x magnification setting on the Nikon 10x/0.3 water objective. The 488 nm laser was used to image nuclei (His-GFP), and the 561 nm laser was used to image transcriptional dots (MCP-mCherry), both at 5% laser power. Exposure time for the green channel was 55 ms and exposure for the red channel was 70 ms. The line illumination tool was used to improve background levels and was set to 40 pixels.

      Spherical aberration was minimized using immersion oil with refractive index (RI) 1.514. 3D image stacks were acquired over the whole nuclear volume in z and with 15 raw images per plane (five phases, three angles). The raw data were computationally reconstructed with SoftWoRx 6.5.2 (GE Healthcare) using channel-specific OTFs recorded using immersion oil with RI 1.512, and Wiener filter settings between 0.002-0.006 to generate 3D stacks of 115 nm (488 nm) or 130 nm (593 nm) lateral and approximately 350 nm axial resolution. Multi-channel acquisitions were aligned in 3D using Chromagnon software (Matsuda et al, 2018) based on 3D-SIM acquisitions of multi-colour EdU-labelled C127 cells(Kraus et al, 2017).
    """


class ImagingMethod(BaseModel):
    value: str
    """The text description of the ontology entry.

    ## Examples
    - bright-field microscopy
    - spinning disk confocal microscopy
    - high-voltage electron microscopy (HVEM)
    """

    ontology_name: str
    """The name of the ontology.

    ## Examples
    - Biological Imaging Methods Ontology (FBbi)
    """

    ontology_id: str
    """The URI identifier for the ontology value.

    ## Examples
    - http://purl.obolibrary.org/obo/FBbi_00000243
    - http://purl.obolibrary.org/obo/FBbi_00000253
    - http://purl.obolibrary.org/obo/FBbi_00000622
    """
