Class dc.Sample.Person Extends (%Persistent, Form.Adaptor)
{

/// Form name, not a global key so it can be anything
Parameter FORMNAME = "Person";

/// Default permissions
/// Objects of this form can be Created, Read, Updated and Deleted
/// Redefine this parameter to change permissions for everyone
/// Redefine checkPermission method (see Form.Security) for this class 
/// to add custom security based on user/roles/etc.
Parameter OBJPERMISSIONS As %String = "CRUD";

/// Property used for basic information about the object
/// By default getObjectDisplayName method gets its value from it
Parameter DISPLAYPROPERTY As %String = "name";

Property name As %VarString(DISPLAYNAME = "Name");

Property surname As %VarString(DISPLAYNAME = "SurName");

Storage Default
{
<Data name="PersonDefaultData">
<Value name="1">
<Value>%%CLASSNAME</Value>
</Value>
<Value name="2">
<Value>name</Value>
</Value>
<Value name="3">
<Value>surname</Value>
</Value>
</Data>
<DataLocation>^dc.Sample.PersonD</DataLocation>
<DefaultData>PersonDefaultData</DefaultData>
<IdLocation>^dc.Sample.PersonD</IdLocation>
<IndexLocation>^dc.Sample.PersonI</IndexLocation>
<StreamLocation>^dc.Sample.PersonS</StreamLocation>
<Type>%Storage.Persistent</Type>
}

}
