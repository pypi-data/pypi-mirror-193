from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File
import os, ctypes

def getCTX(url:str, username:str, password:str) -> ClientContext:
    ctx_auth = AuthenticationContext(url)
    if ctx_auth.acquire_token_for_user(username, password):
        try:
            ctx = ClientContext(url, ctx_auth)
            web = ctx.web
            ctx.load(web)
            ctx.execute_query()
            return ctx
        except:
            raise Exception(f"Error getting CTX: {ctx_auth.get_last_error()}")
    else:
        raise Exception(f"Error getting CTX: {ctx_auth.get_last_error()}")

def downloadFile(ctx:ClientContext, relative_url:str, output_filename:str, output_location:str, hidden:bool=False) -> str:
    os.makedirs(output_location, exist_ok=True)
    if hidden == True:
        FILE_ATTRIBUTE_HIDDEN = 0x02
        ret = ctypes.windll.kernel32.SetFileAttributesW(output_location, FILE_ATTRIBUTE_HIDDEN)
    try:
        with open(output_location + output_filename, 'wb') as output_file:
            response = File.open_binary(ctx, relative_url)
            output_file.write(response.content)
        return output_filename
    except Exception as e:
        raise Exception(f"Error downloading file {output_filename}")

def returnAllContents(ctx:ClientContext, relativeUrl:str, get_files:bool=True, get_folders:bool=False) -> list:
    file_li, folder_li = [], []
    try:
        libraryRoot = ctx.web.get_folder_by_server_relative_url(relativeUrl)
        ctx.load(libraryRoot)
        ctx.execute_query()
    except Exception as e:
        raise Exception('Problem getting directory info')

    if get_folders == True:
        try:
            folders = libraryRoot.folders
            ctx.load(folders)
            ctx.execute_query()
            for myfolder in folders:
                pathList = myfolder.properties["ServerRelativeUrl"].split('/')
                folder_li.append(pathList[-1])
        except Exception as e:
            raise Exception(f"Problem returning folders from {relativeUrl}")

    if get_files == True:
        try:
            files = libraryRoot.files
            ctx.load(files)
            ctx.execute_query()
            for myfile in files:
                pathList = myfile.properties["ServerRelativeUrl"].split('/')
                file_li.append(pathList[-1])
        except Exception as e:
            raise Exception(f"Problem returning files from {relativeUrl}")

    if get_folders == True and get_files == True:
        return [folder_li, file_li]
    elif get_folders == False and get_files == True:
        return file_li
    elif get_folders == True and get_files == False:
        return folder_li
    else:
        return []

def uploadFile(ctx:ClientContext, file:str, filepath:str, rel_path:str) -> None:
    try:
        with open(filepath, 'rb') as content_file:
            file_content = content_file.read()
    except Exception as e:
        raise Exception(f"Error opening {file}")

    try:
        upload = ctx.web.get_folder_by_server_relative_url(rel_path).upload_file(file, file_content).execute_query()
    except Exception as e:
        raise Exception(f"Error uploading {file}")

def deleteFile(ctx:ClientContext, relativeUrl:str) -> None:
    try:
        ctx.web.get_file_by_server_relative_url(relativeUrl).delete_object().execute_query()
    except Exception as e:
        raise Exception(f"Failed to delete the file at {relativeUrl}")

def createFolders(ctx:str, relative_url:str) -> None:
    """creates the path specified on sharepoint"""
    try:
        folder = ctx.web.ensure_folder_path(relative_url).execute_query()
    except Exception as e:
        raise Exception(f"Error creating folder at {relative_url}")

def downloadAllFiles(ctx:ClientContext, rel_url:str, download_dir:str, hidden_dir:bool=False) -> list[str]:
    """downloads all the files within a sharepoint dir - only does root directory of the relative url (no subfolder contents)"""

    try:
        contents = returnAllContents(ctx, rel_url, get_files=True, get_folders=False)
    except Exception as e:
        raise Exception(f"Error getting contents of {rel_url}")
    
    try:
        os.makedirs(download_dir, exist_ok=True)
    except Exception as e:
        raise Exception(f"Error creating {download_dir}")

    for file in contents:
        try:
            downloadFile(ctx, rel_url+"/"+file, file, download_dir, hidden=hidden_dir)
        except Exception as e:
            raise Exception(f"Error downloading {file}")

    return contents