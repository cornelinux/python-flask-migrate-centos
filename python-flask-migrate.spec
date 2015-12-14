%define name python-flask-migrate
%define version 1.5.1
%define unmangled_version 1.5.1
%define release 1

Summary: Flask Migrate
Name: %{name}
Version: %{version}
Release: %{release}
Group: System/Authentication
Prefix: /usr
Provides: flask-sqlalchemy-migrate
#Requires: 
Source0: %{name}-%{version}.tar.gz
License: MIT
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: x86_64
Vendor: Miguel Grinberg
Url: https://github.com/miguelgrinberg/Flask-Migrate

%description
Flask-Migrate is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic. The database operations are provided as command line arguments for Flask-Script.

%prep
%setup -n %{name}-%{version} -n %{name}-%{version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

#%files -f INSTALLED_FILES
%files
/usr/*
%defattr(-,root,root)

