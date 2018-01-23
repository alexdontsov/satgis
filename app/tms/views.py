import math
import traceback
import mapnik

from django.conf import settings
from django.http import HttpResponse
from django.http import Http404

from shapeEditor.shared.models import Shapefile
from shapeEditor.shared import utils
