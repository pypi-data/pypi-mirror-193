"""
Use the `AdminConfig` object to invoke configuration commands and to create or 
change elements of the WebSphere® Application Server configuration, for example, 
creating a data source.

For more info see the [official documentation](https://www.ibm.com/docs/en/was-nd/8.5.5?topic=scripting-commands-adminconfig-object-using-wsadmin).
"""
from typing import Any, Optional, Union, overload

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

# --------------------------------------------------------------------------
@overload
def list(object_type: ResourceType, /) -> MultilineList[ConfigurationObjectName]:
    """Lists all the configuration objects of the type named by `object_type`.

    Args:
        object_type (ResourceType): The name of the object type.

    Returns:
        objects(MultilineList[ConfigurationObjectName]): Multiline list of objects of the given type.
    """
    ...

@overload
def list(object_type: ResourceType, scope: ConfigurationObjectName, /) -> MultilineList[ConfigurationObjectName]:
    """Lists all the configuration objects of the type named by `object_type` in the scope of `scope`.

    Args:
        object_type (ResourceType): The name of the object type.
        scope (ConfigurationObjectName): The scope of the search.

    Returns:
        objects(MultilineList[ConfigurationObjectName]): Multiline list of objects of the given type found under the scope of `scope`.
    """
    ...

@overload
def list(object_type: ResourceType, pattern: str, /) -> MultilineList[ConfigurationObjectName]:
    """Lists all the configuration objects of the type named by `object_type` and matching 
    wildcard characters or Java regular expressions.

    Args:
        object_type (ResourceType): The name of the object type.
        pattern (str): The pattern (wildcard characters or Java regular expressions) that needs to be matched.

    Returns:
        objects(MultilineList[ConfigurationObjectName]): Multiline list of objects of the given type matching the pattern `pattern`
    """
    ...

def list(object_type: ResourceType, scope_or_pattern: Optional[Union[ConfigurationObjectName, str]] = "", /) -> MultilineList[ConfigurationObjectName]: # type: ignore[misc]
    """Lists all the configuration objects of the type named by `object_type`.
    
    Args:
        object_type (ResourceType): The name of the object type.
        scope_or_pattern (Union[ConfigurationObjectName, str], optional): This parameter causes a different behaviour depending on its type:
            
            - `ConfigurationObjectName`: Limit the search within the scope of the configuration object named by `scope`.
            - `str`: Search all the configuration objects matching wildcard characters or Java regular expressions.

    Returns:
        objects(MultilineList[ConfigurationObjectName]): Multiline list of objects of a given type, possibly scoped by a parent.
    
    Example:
        If the `scope_or_pattern` parameter is omitted, then will be returned a list of all servers defined:
        ```pycon
        >>> print(AdminConfig.list("Server"))
        ```

        You can narrow the search using the `scope_or_pattern` parameter:

        - Limit the search to only the servers under the **scope** of the node `node`:
            ```pycon
            >>> node = AdminConfig.list("Node").splitlines()[0]
            >>> print(AdminConfig.list("Server", node))
            ```
        - Search the servers matching a specific **wildcard** pattern:
            ```pycon
            >>> print(AdminConfig.list("Server", "server1*"))
            ```
        - Search the servers matching a specific **regular expression** pattern:
            ```pycon
            >>> print(AdminConfig.list("Server", "server1.*"))
            ```
    """
    ...
# --------------------------------------------------------------------------

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

# --------------------------------------------------------------------------
@overload
def types() -> MultilineList[ResourceType]:
    """Displays all the possible top-level configuration object types.

    Returns:
        types(MultilineList[ResourceType]): All the top-level configuration object types.
    """
    ...

@overload
def types(pattern: str) -> MultilineList[ResourceType]:
    """Displays all the possible top-level configuration object types matching
    with the `pattern`, which can be a wildcard or a regular expression.

    Args:
        pattern (str): A wildcard or a regular expression matching the type to search.

    Returns:
        types(MultilineList[ResourceType]): A multiline list of all the possible top-level configuration object types
            matching the provided `pattern`.
    """
    ...

def types(pattern: Optional[str] = "") -> MultilineList[ResourceType]: # type: ignore[misc]
    """Displays all the possible top-level configuration object types, restricting the 
    search to the types matching the `pattern` parameter, if specified.

    Args:
        pattern (Optional[str], optional): A wildcard or a regular expression matching the type to search.
    
    Returns:
        types(MultilineList[ResourceType]): A multiline list of all the possible top-level configuration object types
            matching the provided `pattern` (if specified).

    Example:
        - Print **all** the available types:
            ```pycon
            >>> print(AdminConfig.types())
                AccessPointGroup
                Action
                ActivationSpec
                ActivationSpecTemplateProps
                ActiveAffinityType
                [...]
            ```
        - Print **only** the types matching the regex `No.*`:
            ```pycon
            >>> print(AdminConfig.types("No.*"))
                NoOpPolicy
                Node
                NodeAgent
                NodeGroup
                NodeGroupMember
            ```
    """
    ...
# --------------------------------------------------------------------------

def uninstallResourceAdapter(): # undocumented
    ...

def unsetAttributes(): # undocumented
    ...

def validate(): # undocumented
    ...
