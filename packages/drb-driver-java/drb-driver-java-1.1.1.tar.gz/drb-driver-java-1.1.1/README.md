# JavaNode driver
The drb-driver-java python module aims to wrap Java version of DRB model. It is able to navigates among java nodes content.

See [documentation]() for details.
# Library usage 
Java must be present in the system

Normally if java is correctly installed, the ``JAVA_HOME`` environment _variable_ is set
You can check it by command line below

```commandline
echo $JAVA_HOME
```

Installing this library with execute the following in a terminal
```commandline
pip install drb-driver-java
```

If you want add schema or addon you have eventually ``CLASSPATH_ADDON`` to define    
```commandline
export CLASSPATH_ADDON=/path_addon_one/*;
```

## Java Factory and Java Node
The module implements the basic factory model defined in DRB in its node resolver. Based on the python entry point mechanism, this module can be dynamically imported into applications.

The entry point group reference is `drb.driver`.<br/>
The driver name is `java`.<br/>
The factory class `DrbJavaFactory` is encoded into `drb.drivers.factory`

The java factory creates a JavaNode from an existing java content. It uses a base node to access the content data using a streamed implementation from the base node.

The base node can be a DrbFileNode, DrbHttpNode, DrbTarNode or any other nodes able to provide streamed (`BufferedIOBase`, `RawIOBase`, `IO`) java content.
## limitations
The current version does not manage child modification and insertion. JavaNode is currently read only.
## Using this module
To include this module into your project, the `drb-driver-java` module shall be referenced into `requirements.txt` file, or the following pip line can be run:
```commandline
pip install drb-driver-java
```
Set eventually environment variable ``CLASSPATH_ADDON`` and ``JAVA_HOME``

[documentation]: https://drb-python.gitlab.io/impl/java