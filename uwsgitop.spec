Summary:	uWSGI top-like application
Name:		uwsgitop
Version:	0.6.2
Release:	1
License:	MIT
Group:		Networking/Admin
Source0:	https://pypi.python.org/packages/source/u/uwsgitop/%{name}-%{version}.tar.gz
# Source0-md5:	eabb727d79d6d3d2c838430987f5f327
URL:		https://github.com/unbit/uwsgitop
BuildRequires:	sed >= 4.0
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
uwsgitop is a top-like command that uses the uWSGI stats server.

%prep
%setup -q

%{__sed} -i -e '1s,^#!.*python,#!%{__python},' uwsgitop

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

install uwsgitop $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/uwsgitop
