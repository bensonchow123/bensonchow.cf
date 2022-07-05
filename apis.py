import praw
import os

from dotenv import load_dotenv
from flask import Blueprint, jsonify, request

load_dotenv()
apis = Blueprint("apis",__name__)