from typing import Generic, List, Protocol, TypeVar

class OpaqueDigestObject(object):
    """
    Opaque "digest" object returned by a call to the `AdminConfig.extract()` method.
    
    Question: More testing needed
        I **didn't test this command** in my test environment but i will need to, in order to better understand it.
    """
    ...

T = TypeVar('T', bound=str)

class MultilineList(str, Generic[T]):
    """ A `wsadmin` response which is composed of a multiline string representing a list of values. 

        To get the original value use the `splitlines()` method.

        This class is meant to be used as a type, and takes another type in input
            which represents the **type of each line** of the text (i.e. `MultilineList[RunningObjectName]`).

        !!! Info "History background"
            This type of output (instead of an actual `list`) is a legacy from the **JACL**  coding style.

            The administrative API was written with Jacl in mind. 
            With Jython one you have to do tricks like this one to get server list as list:

            ```python
            for srv in AdminConfig.list('Server').splitlines():
                print srv
            ```

            Whereas in Jacl one can simply do this:

            ```tcl
            foreach srv [$AdminConfig list Server] {
                puts $srv
            }
            ```

            Obviously, many [`AdminConfig`](/reference/wsadmin_type_hints/AdminConfig) and [`AdminControl`](/reference/wsadmin_type_hints/AdminControl) methods return lists as newline-separated string.

            [_Source_](https://stackoverflow.com/a/12910544/8965861)

        Example:
            To use it you must pass the multiline type between square brackets:
            ```pycon
            >>> from wsadmin_type_hints.typing_objects.wsadmin_types import MultilineList
            >>> from wsadmin_type_hints.typing_objects.object_name import RunningObjectName
            >>> 
            >>> result: MultilineList[RunningObjectName] = ""
            ```
    """
    def splitlines(self, keepends: bool = ..., /) -> List[T]: ... # type: ignore