#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-commons-el
Version  : 1.0
Release  : 1
URL      : https://repo1.maven.org/maven2/commons-el/commons-el/1.0/commons-el-1.0.jar
Source0  : https://repo1.maven.org/maven2/commons-el/commons-el/1.0/commons-el-1.0.jar
Source1  : https://repo1.maven.org/maven2/commons-el/commons-el/1.0/commons-el-1.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-1.1
Requires: mvn-commons-el-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-commons-el package.
Group: Data

%description data
data components for the mvn-commons-el package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-el/commons-el/1.0
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/commons-el/commons-el/1.0/commons-el-1.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/commons-el/commons-el/1.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/commons-el/commons-el/1.0/commons-el-1.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/commons-el/commons-el/1.0/commons-el-1.0.jar
/usr/share/java/.m2/repository/commons-el/commons-el/1.0/commons-el-1.0.pom
