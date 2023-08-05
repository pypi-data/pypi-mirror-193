# -*- coding: utf-8 -*-

import os
import sys
import shlex
import logging
import argparse
import subprocess as sp

from pathlib import Path

from .mute import null
from .mute import thunder_dummy
from .mute.page import _js
from .mute.page import _css
from .mute.page import _html
from .mute.app import app_admin_dummy
from .mute.app import app_forms_dummy
from .mute.app import app_models_dummy
from .mute.app import app_views_dummy
from .mute.project import pro_init_dummy
from .mute.project import pro_config_dummy
from .mute.project import pro_routes_dummy
from .mute.auth import auth_init_dummy
from .mute.auth import auth_forms_dummy
from .mute.auth import auth_models_dummy
from .mute.auth import auth_routes_dummy
from . import __title__
from . import __version__

"""
  NOTSET    ---  0
  DEBUG     ---  10
  INFO      ---  20
  WARNING   ---  30  (default)
  ERROR     ---  40
  CRITICAL  ---  50
"""

formatter = "[+] [%(asctime)s] [%(levelname)s] %(message)s"
logging.basicConfig(format = formatter)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# used for relative path to default image to copy for a project (only)
ORIGIN = Path(__file__).resolve().parent


class BaseStructure:
  """base structure class"""

  def __init__(self, is_software=True):
    """base structure class initializer"""
    self.is_software = is_software
    self.fls_cmd = "touch"
    self._exs_first = ["index", "style"]
    self._exs_last = [".html", ".css", ".js"]
    

  def append_exs_to_file(self, fls_name=False, _exs_=".py", name=None):
    """append .py extension for files if _exs_ value is ".py" or type is str, else if _exs_ type is list, make list of static files `['index.html', 'index.js', 'style.css']` """

    if type(_exs_) == list:
      name, exst = self._exs_first, self._exs_last
      lst = []
      
      for i in exst:
        if i == exst[1]: # css
          idx = name[1]
          lst.append(f"{idx}{i}")
        if i == exst[0] or i == exst[2]: # html & js
          for j in exst:
            if j != exst[1]:
              idx = name[0]
              if f"{idx}{j}" in lst:
                pass
              else:
                lst.append(f"{idx}{j}")
      return lst
    if type(_exs_) == str:
      return [i+f"{_exs_}" for i in fls_name]
      

  def file_content(self, _exs=False, content=None, file_name="index", dir_togo=None, route_go=True):
    """insert content in a file"""
    if _exs:
      with open(f"{file_name}{_exs}", "w") as pay_fls:
        pay_fls.write(f"{content}")
    else:
      with open(f"{file_name}", "w") as pay_fls:
        pay_fls.write(f"{content}")
    if route_go:
      os.chdir(dir_togo)
      

  def file_opt(self, _dir, tree=True, _here=False, _where=False):
    """make tree dir if `tree=True` and get into it, if `_here` or `_where` is equal to True"""
    if tree:
      sp.run(["mkdir", "-p", _dir])
    if _here:
      os.chdir(os.path.join(_here, _dir))
    if _where:
      os.chdir(_where)
      

  def into_file(self, fls, fls_cmd, file=None, app_default_dummy=null(), is_static_file=False, is_app=False, proj_nm=None):
    """create files within current directory of '''self.file_opt()'''
    is_app: if it is True, that mean it will do operation of making app files,
    else it will make for the entire project
    """
    
    if is_app:
      for _fls in fls:
        app_name = os.getcwd().split('/')[-1]
        sp.run(shlex.split(f"{fls_cmd} {_fls}"))
        if is_static_file:
          # building app default files
          self.file_content(file_name=_fls, content=f"{app_default_dummy}", route_go=False)
        else:
          if _fls == "__init__.py":
            # building app `__init__.py` default files
            self.file_content(file_name=_fls, content=f"# from {__title__} software, your app ({app_name}) {_fls} file\n{null()}", route_go=False)

          elif _fls == "forms.py":
            # building app `forms.py` default files
            self.file_content(file_name=_fls, content=f"# from {__title__} software, your app ({app_name}) {_fls} file\n{app_forms_dummy(app_name)}", route_go=False)

          elif _fls == "models.py":
            # building app `models.py` default files
            self.file_content(file_name=_fls, content=f"# from {__title__} software, your app ({app_name}) {_fls} file\n{app_models_dummy(self.proj_store_name, app_name=app_name)}", route_go=False)
            
          elif _fls == "views.py":
            # building app `views.py` default files
            self.file_content(file_name=_fls, content=f"# from {__title__} software, your app ({app_name}) {_fls} file\n{app_views_dummy(app_name)}", route_go=False)
            
          elif _fls == "admin.py":
            # building app `admin.py` default files
            self.file_content(file_name=_fls, content=f"# from {__title__} software, your app ({app_name}) {_fls} file\n{app_admin_dummy(app=app_name)}", route_go=False)
    else:
      for _fls in fls:
        if _fls[:-3] == file:
          sp.run(shlex.split(f"{fls_cmd} {_fls}"))
          self.file_content(
            file_name=_fls,content=f"# Your project {_fls} file\n{thunder_dummy(proj_nm)}", route_go=False
            ) # building the run module
            

  def dir_tree(self, proj_name=None):
    """create a directory tree where file will reserved as well as modules too"""
    dirs = [proj_name, f"{proj_name}/{proj_name}", f"{proj_name}/auth", "templates", "static"]

    # default files of project auth folder, which is for project base dir
    auth_models = ["__init__", "models", "forms", "routes"]
    auth_fls = self.append_exs_to_file(fls_name=auth_models)
    
    # default files of project sub folder, except `thunder` which is for project base dir
    fls_name = ["__init__", "config", "routes", "thunder"]
    fls = self.append_exs_to_file(fls_name=fls_name) # appending extensions to files
    _here = os.getcwd() # initial `cwd` where the project was e.g `Desktop`
    
    # check if the project already exist
    if os.path.exists(os.path.join(_here, proj_name)):
      print(f"\nProject ({proj_name}) already exist in this directory\n\t" + os.path.realpath(proj_name))
      logger.info(_here)
      print()
    else:
      # making directories trees and their default files in the loop
      for _dir in dirs:
        if _dir == dirs[0] + "/" + dirs[0]:
          self.file_opt(_dir, _here=_here)
          # create default modules inside project sub dir
          for _fls in fls:
            if _fls[:-3] != "thunder":
              sp.run(shlex.split(f"{self.fls_cmd} {_fls}"))
              if _fls == "__init__.py":
                # building project `__init__.py` default files
                self.file_content(file_name=_fls, content=f"# from {__title__} software, your ({proj_name}) project {_fls} file\n{pro_init_dummy()}", route_go=False)

              elif _fls == "config.py":
                # building project `config.py` default files
                self.file_content(file_name=_fls, content=f"# from {__title__} software, your ({proj_name}) project {_fls} file\n{pro_config_dummy(proj_name)}", route_go=False)

              elif _fls == "routes.py":
                # building project `routes.py` default files
                self.file_content(file_name=_fls, content=f"# from {__title__} software, your ({proj_name}) project {_fls} file\n{pro_routes_dummy(proj_name)}", route_go=False)
          os.chdir(_here)

         
        if _dir == dirs[2]:
          self.file_opt(_dir, _here=_here)
          # create default modules inside project auth dir
          for _fls in auth_fls:
            sp.run(shlex.split(f"{self.fls_cmd} {_fls}"))
            if _fls == "__init__.py":
              # building project `__init__.py` default files
              self.file_content(file_name=_fls, content=f"# from {__title__} software, your ({proj_name}) project {_fls} file\n{auth_init_dummy()}", route_go=False)

            elif _fls == "forms.py":
              # building project `forms.py` default files
              self.file_content(file_name=_fls, content=f"# from {__title__} software, your ({proj_name}) project {_fls} file\n{auth_forms_dummy()}", route_go=False)

            elif _fls == "models.py":
              # building project `models.py` default files
              self.file_content(file_name=_fls, content=f"# from {__title__} software, your ({proj_name}) project {_fls} file\n{auth_models_dummy(proj_name)}", route_go=False)

            elif _fls == "routes.py":
              # building project `routes.py` default files
              self.file_content(file_name=_fls, content=f"# from {__title__} software, your ({proj_name}) project {_fls} file\n{auth_routes_dummy(proj_name)}", route_go=False)
          os.chdir(_here) 
        if _dir == dirs[0]:
          self.file_opt(_dir, _here=_here)
          self.into_file(fls, self.fls_cmd, file="thunder", proj_nm=proj_name) # to maker thunder file
          project_folder = os.getcwd() # base dir path of 
          
          for static_dir in dirs[3:]: # templates & static
            if static_dir == dirs[3:][0]: # templates
              self.file_opt(static_dir, _here=project_folder) # make templates dir and cd into it
              
              templates_folder = os.getcwd() # base dir path of templates folder
              
              # make project dir in templates and cd into it 
              self.file_opt(proj_name, _here=templates_folder)
              # create project index.html and back to templates base dir path
              self.file_content(self._exs_last[0], content=f"<!-- @{__title__}, {proj_name} (project) index.html page -->\n"+_html(proj_name, is_base=False), dir_togo=templates_folder)

              # make project dir in templates and cd into it 
              self.file_opt("admin", _here=templates_folder)
              # create project admin index.html and back to project base dir path
              self.file_content(self._exs_last[0], content=f"<!-- @{__title__}, {proj_name} (project) admin index.html page -->\n"+_html("do_nothing", admin=True, project_name=proj_name), dir_togo=project_folder)
              
            if static_dir == dirs[3:][1]: # static
              self.file_opt(static_dir, _here=project_folder) # make static dir and cd into
              
              # make project static dir and cd into, NB: `os.getcwd()` is base dir of static dir
              self.file_opt(proj_name, _where=os.getcwd()+"/"+proj_name)

              # storing the project static dir path before creating any thing and cd into media
              s_p_dir = os.getcwd()
              self.file_opt("media", _where="media") # make media dir for project
              self.file_opt("do_nothing", tree=False, _where=s_p_dir)
              """
              # :going back with one step

              we pass `do_nothing` as a directory name here, to avoid any
              error even though it do nothing if we give it a real directory name
              """

              self.file_content(self._exs_last[1], file_name="style", content=f"/* @{__title__}, {proj_name} (project) style.css file */\n"+_css(), route_go=False) # create style.css
              
              # create index.js and back to project static base dir path
              self.file_content(self._exs_last[2], content=f"// @{__title__}, {proj_name} (project) index.js file\n"+_js(proj_name), dir_togo=project_folder)

          os.chdir(_here)
      print()
      logger.info(f"Project ({proj_name}) created successfully!")
      print()
      

class AppStructure(BaseStructure):
  """base structure class"""
  app_store_name = None # app name
  proj_store_name = None # project name
  
  def app_static_and_template(self, file_dummy, top_comment=False, _dir_=False, file=False, app=False, cmd=False, _here_=False):
    # :_dir_ = "template or static"
    # :file = ["index.html"]
    # :app = app name
    # :cmd = "touch"
    # :_here_ = # initial `inside project folder` where the project was created
    if top_comment == "html":
      top_comment = f"<!-- @{__title__}, {app} {file[0]} page -->\n"
    if top_comment == "css":
      top_comment = f"/* @{__title__}, {app} {file[0]} file */\n"
    if top_comment == "js":
      top_comment = f"// @{__title__}, {app} {file[0]} file\n"
      
    self.file_opt(_dir_, tree=False, _here=_here_) # back to template dir
    self.file_opt(f"{app}", _where=app) # make app dir inside `template`
    self.into_file(file, cmd, is_static_file=True, app_default_dummy=f"{top_comment}{file_dummy}", is_app=True) # making app default file
    
    
  def dir_tree(self, proj_app_name=None):
    """create a directory tree where file will reserved as well as modules too"""
    
    dirs = [proj_app_name]
    app_store_name = proj_app_name # store our app name
    fls_name = ["__init__", "views", "models", "forms", "admin"]
    fls = self.append_exs_to_file(fls_name=fls_name)
    roove_dir = ["templates", "static", "static"]
    _here_app = os.getcwd()  # initial `inside project folder` where the project was created
    
    # check if the app already exist
    app_proj_name = _here_app.split("/")[-1]
    self.proj_store_name = app_proj_name

    if os.path.exists(os.path.join(_here_app, proj_app_name)):
      print(f"\nApp ({proj_app_name}) already exist in this project ({app_proj_name})\n\t" + os.path.realpath(proj_app_name))
      logger.info(_here_app)
      print()
    else:
      # making directories trees and their default files
      for _dir in dirs:
        if _dir == dirs[0]:
          self.file_opt(_dir, _here=_here_app)
          self.into_file(fls, self.fls_cmd, is_app=True) # to maker app default files
          
      self.app_static_and_template(
        _html(app_store_name, project_name=self.proj_store_name), top_comment="html", _dir_=roove_dir[0], file=[self.append_exs_to_file(_exs_=[])[0]], app=proj_app_name, cmd=self.fls_cmd, _here_=_here_app
        )
      self.app_static_and_template(
        _css(), top_comment="css", _dir_=roove_dir[1], file=[self.append_exs_to_file(_exs_=[])[2]], app=proj_app_name, cmd=self.fls_cmd, _here_=_here_app
        )
      self.app_static_and_template(
        _js(proj_app_name), top_comment="js", _dir_=roove_dir[2], file=[self.append_exs_to_file(_exs_=[])[1]], app=proj_app_name, cmd=self.fls_cmd, _here_=_here_app
        )
      self.file_opt("media") # an app media folder
      self.file_opt("do_nothing", tree=False, _where=_here_app) # back to project dir
      print()
      logger.info(f"App ({proj_app_name}) created successfully! in {app_proj_name}")
      print()
      

def app_init(app):
  """initialize app in project"""
  AppStructure().dir_tree(app)
  exit()
  

class Boot:
  """boot up project operation, app operation, and the server"""
  def __init__(self, p=None, d=False, h=None, db=None, model=None):
    self.p = p # port
    self.d = d # debug
    self.h = h # host
    self.db = db
    self.model = model

  def run(self):
    """run method for creating app and booting up server"""
    
    error_ref_1 = f"""\n Run the command with one of this positional arguments:\n\tcreate_app   ---   ( for creating an app within your project )\n\tboot  ---   ( for booting up your server )"""

    error_ref_2 = f"""
 create_app:
    usage: create_app [-h] --app  [--debug]

    This create an app in your project

    positional arguments:
                    Put positional argument of `create_app` to create app, app are create inside your project

    optional arguments:
      -h, --help     show this help message and exit
      --app , -a     What is the app name

 boot:
    usage: boot up server [-h] [--port] [--host] [--debug]

    This boot up the server

    positional arguments:
                    Put positional argument of `boot` to bring server up running

    optional arguments:
      -h, --help     show this help message and exit
      --port , -p    What is the port number?
      --host , -H    What is the host?
      --debug , -d   Do you want debug?"""
    if len(sys.argv) == 1:
      print()
      logger.error(f"please run the module with positional argument and flag if needed\n{error_ref_1}")
      exit()

    if sys.argv[1] == "create_app":
      # prog is the name of the program, default=sys.argv[0]
      parser = argparse.ArgumentParser(prog="create_app", description="This create an app in your project")
      # metavar make the -help to look cleaan
      parser.add_argument("--app", "-a", required=True, type=str, metavar="", help="What is the app name")
      parser.add_argument(dest="create_app", default="create_app", type=str, metavar="", help="Put positional argument of `create_app` to create app, app are create inside your project")
      args = parser.parse_args()
      the_proj = os.getcwd().split('/')[-1]
      
      if args.app.lower() == __title__:
        print()
        logger.error(f"Not allowed to use ({__title__}) package name as an app name\n")
        exit()
      elif args.app == the_proj:
        print()
        logger.error(f"Not allowed to use your ({the_proj}) project name as an app name\n")
        exit()
      app_init(args.app)

    elif sys.argv[1] == "boot":
      parser = argparse.ArgumentParser(prog="boot up server", description="This boot up the server")
      parser.add_argument("--port", "-p", default=5000, required=False, type=int, metavar="", help="What is the port number?")
      parser.add_argument("--host", "-H", default=self.h, required=False, type=str, metavar="", help="What is the host?")
      parser.add_argument("--debug", "-d", default=False, required=False, type=bool, metavar="", help="Do you want debug?")
      parser.add_argument(dest="boot", default="boot", type=str, metavar="", help="Put positional argument of `boot` to bring server up running")
      args = parser.parse_args()
      self.p = args.port
      self.h = args.host
      self.d = args.debug
      
      # logger.info(f"@{__title__} v{__version__} | visit: http://localhost:{args.port} (for development)")
    elif sys.argv[1] == "create_user":
      from .utils import AuthCredentials

      auth_class = AuthCredentials().result
      username = auth_class[0]
      email = auth_class[1]
      password = auth_class[2]

      u = self.model(username=username, email=email, password=password)

      self.db.session.add(u)
      self.db.session.commit()
      logger.info(f"One record added ({username})")
      exit()
    else:
      print()
      logger.error(f"use a valid positional argument and flag if needed\n{error_ref_2}")
      exit()
