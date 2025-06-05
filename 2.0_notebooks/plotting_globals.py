# ---- Global parameters for font type, sizes, titles, and figure sizes ----
FONT_FAMILY = "DejaVu Sans"
TITLE_FONT_SIZE = 24
LEGEND_FONT_SIZE = 11
LEGEND_TITLE_FONT_SIZE = 12
ANNOTATION_FONT_SIZE = 11
FIGSIZE_COMBINED = (44, 16)   # For side-by-side (1,2) plots
FIGSIZE_SINGLE = (22, 16)     # For single map plots

GLOBAL_FIGSIZE = FIGSIZE_SINGLE
GLOBAL_LABEL_FONTSIZE = ANNOTATION_FONT_SIZE
GLOBAL_TITLE_FONTSIZE = TITLE_FONT_SIZE
GLOBAL_CITY_LABEL_FONTSIZE = ANNOTATION_FONT_SIZE
GLOBAL_CITY_LABEL_FONTSIZE_UTRECHT = ANNOTATION_FONT_SIZE + 5

# --- City coordinates for annotation ---
GLOBAL_CITY_COORDS = {
    "UTRECHT": (136784, 455860),
    "Amersfoort": (155041, 463103),
    "Nieuwegein": (133952, 448951),
    "Houten": (139963, 448940),
    "Zeist": (144446, 455827),
    "Veenendaal": (166571, 448709)
}

GLOBAL_CITY_LABEL_OFFSETS = {
    "UTRECHT": (0, 9000),
    "Zeist": (0, 9000),
    "Amersfoort": (8000, 4000),
    "Nieuwegein": (-8000, -5000),
    "Houten": (6000, -6000),
    "Veenendaal": (5000, 1000)
}

# --- Add Utrecht pictogram image to the corner of the map ---
# Use the pictogram at OUTPUT_DIR/pictogram.png
pictogram_path = OUTPUT_DIR / "pictogram.png"
if pictogram_path.exists():
    img = mpimg.imread(str(pictogram_path))
    imagebox = OffsetImage(img, zoom=0.18, resample=True)
    # Place pictogram just below the legend, outside the axes
    # The legend is at (1.18, 1), so pictogram at (1.18, 0.13) (tweak as needed)
    ab = AnnotationBbox(
        imagebox,
        (1.28, 0.13),  # (x, y) in axes fraction, moved more to the right
        xycoords='axes fraction',
        frameon=False,
        box_alignment=(1, 0)
    )
    ax.add_artist(ab)
else:
    print(f"No pictogram file found at {pictogram_path.resolve()}")