import os
import pathlib
from pathlib import Path

WOODS = ["acacia", "bamboo", "birch", "cherry", "crimson", "dark_oak", "jungle", "mangrove", "oak", "spruce", "warped"]

PLACEHOLDER="$WOOD"

TEMPLATE_DIR = Path("templates")
OUTPUT_DIR = Path("data/mcplus/recipes")

templates = [item for item in pathlib.Path("templates").rglob("*.json") if item.is_file()]

for template_path in templates:
  template = template_path.read_text()
  rel_path = os.path.relpath(template_path, TEMPLATE_DIR)

  for wood in WOODS:
    templated_path = os.path.join(OUTPUT_DIR, rel_path)
    output_file = Path(str(templated_path).replace(PLACEHOLDER, wood))
    output_contents = template.replace(PLACEHOLDER, wood)

    output_file.parent.mkdir(exist_ok=True, parents=True)
    output_file.write_text(output_contents)