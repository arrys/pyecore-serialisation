# PyEcore Serialisation

Small example to replicate a (de)serialisation bug in PyEcore.

> Generate the required ecore python static files first if they're not present: ´pyecoregen -e example/min.ecore -o example/´.

We run the deserialization -> serialization steps twice.

The original file looks like this:

    <?xml version="1.0" encoding="UTF-8"?>
    <EXAMPLE:Example xmi:version="2.0" xmlns:xmi="http://www.omg.org/XMI" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:EXAMPLE="http://www.example.org/EXAMPLE">
        <values>1.0</values>
        <values>2.0</values>
        <values>3.0</values>
    </EXAMPLE:Example>


After the first step:

    <?xml version='1.0' encoding='UTF-8'?>
    <EXAMPLE:Example xmlns:xmi="http://www.omg.org/XMI" xmlns:EXAMPLE="http://www.example.org/EXAMPLE" values="1.0 2.0 3.0" xmi:version="2.0"/>

After the second step:

    <?xml version='1.0' encoding='UTF-8'?>
    <EXAMPLE:Example xmlns:xmi="http://www.omg.org/XMI" xmlns:EXAMPLE="http://www.example.org/EXAMPLE" values="[]" xmi:version="2.0"/>

At this point a third step will fail on the deserialization part.
