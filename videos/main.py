#!/usr/bin/env python

# Python Standard Library
import os
from pathlib import Path
from typing import Optional

# First-Party Librairies
import pandoc

# Third-Party Librairies
from plumbum import FG
from plumbum.cmd import python


python["attractivity.py"] & FG
python["hausdorff.py"] & FG
python["asymptotic-stability.py"] & FG
python["vinograd-point.py"] & FG
python["lti-balls.py"] & FG
python["vinograd-ball.py"] & FG
python["vinograd-compact.py"] & FG