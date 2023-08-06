"""
Use the `AdminConfig` object to invoke configuration commands and to create or 
change elements of the WebSphere® Application Server configuration, for example, 
creating a data source.

For more info see the [official documentation](https://www.ibm.com/docs/en/was-nd/8.5.5?topic=scripting-commands-adminconfig-object-using-wsadmin).
"""
from typing import Any

from wsadmin_type_hints.typing_objects.object_name import ConfigurationObjectName
from .typing_objects.wsadmin_types import MultilineList, OpaqueDigestObject
from .typing_objects.literals import ResourceType

def attributes(object_type: ResourceType, /) -> str:
    """Get a multiline string containing the top level attributes for the given type.

    Args:
        object_type (str): name of the object type. Use `AdminConfig.types()` to get a list of available types.

    Returns:
        str: Multiline string with the top level attributes for the given type.
    """
    ...

# TODO: Check return type
def checkin(document_uri: str, file_name: str, opaque_object: OpaqueDigestObject, /) -> Any:
    """Checks a file that the document URI describes into the configuration repository.
    This method only applies to deployment manager configurations.

    Args:
        document_uri (str): The document URI, relative to the root of the configuration repository.
        file_name (str): The name of the source file to check.
        opaque_object (OpaqueDigestObject): The object returned by a prior call to the `AdminConfig.extract()` command.
    
    Question: More testing needed
        The **return type** needs to be checked.
    """
    ...

def convertToCluster(): # undocumented
    ...

def create(): # undocumented
    ...

def createClusterMember(): # undocumented
    ...

def createDocument(): # undocumented
    ...

def createUsingTemplate(): # undocumented
    ...

def defaults(): # undocumented
    ...

def deleteDocument(): # undocumented
    ...

def existsDocument(): # undocumented
    ...

def extract(document_uri: str, filename: str, /) -> OpaqueDigestObject:
    """Extracts a configuration repository file that is described by the document URI and places it in the file named by filename. 
    This method only applies to deployment manager configurations.

    Args:
        document_uri (str): The document URI, relative to the root of the configuration repository. This MUST exist in the repository.
        filename (str): The name of the source file to check. If it exists already, it will be overwritten.

    Returns:
        OpaqueDigestObject: An opaque "digest" object which should be used to check the file back in using the checkin command.
    """
    ...

def getCrossDocumentValidationEnabled(): # undocumented
    ...

def getid(): # undocumented
    ...

def getObjectName(): # undocumented
    ...

def getObjectType(): # undocumented
    ...

def getSaveMode(): # undocumented
    ...

def getValidationLevel(): # undocumented
    ...

def getValidationSeverityResult(): # undocumented
    ...

def hasChanges(): # undocumented
    ...

def help(): # undocumented
    ...

def installResourceAdapter(): # undocumented
    ...

def list(object_type: ResourceType, pattern="", /) -> MultilineList[ConfigurationObjectName]:
    """Use the list command to return a list of objects of a given type, possibly scoped by a parent.
    
    Args:
        object_type (ResourceType): The name of the object type.
        pattern (str, optional): Additional search query information using wildcard characters or Java regular expressions. Defaults to "".

    Returns:
        MultilineList[ConfigurationObjectName]: Multiline list of objects of a given type, possibly scoped by a parent.
    
    Example:
        If the `pattern` parameter is omitted, then will be returned a list of all servers defined:
        ```pycon
        >>> print(AdminConfig.list("Server"))
        ```

        You can narrow the scope by using:

        - Wildcard patterns:
            ```pycon
            >>> print(AdminConfig.list("Server", "server1*"))
            ```
        - Regular expression patters:
            ```pycon
            >>> print(AdminConfig.list("Server", "server1.*"))
            ```
        - Complete [ConfigurationObjectName][wsadmin_type_hints.typing_objects.object_name.ConfigurationObjectName]:
            ```pycon
            >>> node = AdminConfig.list("Node").splitlines()[0]
            >>> print(AdminConfig.list("Server", node))
            ```
    """
    ...

def listTemplates(): # undocumented
    ...

def modify(): # undocumented
    ...

def parents(): # undocumented
    ...

def queryChanges(): # undocumented
    ...

def remove(): # undocumented
    ...

def required(): # undocumented
    ...

def reset(): # undocumented
    ...

def resetAttributes(): # undocumented
    ...

def save(): # undocumented
    ...

def setCrossDocumentValidationEnabled(): # undocumented
    ...

def setSaveMode(): # undocumented
    ...

def setValidationLevel(): # undocumented
    ...

def show(): # undocumented
    ...

def showall(): # undocumented
    ...

def showAttribute(): # undocumented
    ...

def types(): # undocumented
    ...

def uninstallResourceAdapter(): # undocumented
    ...

def unsetAttributes(): # undocumented
    ...

def validate(): # undocumented
    ...
