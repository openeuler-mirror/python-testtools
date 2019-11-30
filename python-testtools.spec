Name:           python-testtools
Version:        2.3.0
Release:        10
Summary:        Extensions to the Python unit testing framework
License:        MIT
URL:            https://launchpad.net/testtools
Source0:        https://pypi.io/packages/source/t/testtools/testtools-%{version}.tar.gz

Patch0001:      testtools-1.8.0-py3.patch
Patch0002:      testtools-2.3.0-py37.patch

BuildRequires:  python2-devel python2-extras python2-mimeparse >= 0.1.4 python2-pbr python2-setuptools
BuildRequires:  python2-unittest2 >= 1.0.0 python2-traceback2 python2-testscenarios python3-devel
BuildRequires:  python3-extras python3-mimeparse python3-pbr python3-setuptools python3-unittest2
BuildRequires:  python3-traceback2 python3-testscenarios python2-sphinx
BuildArch:      noarch

%description
Testtools is a set of extensions to the Python standard library's unit testing framework. These
extensions have been derived from years of experience with unit testing in Python and come from
many different sources.

%package -n python2-testtools
Summary:        Extensions to the Python unit testing framework
Requires:       python2-extras python2-mimeparse python2-pbr python2-unittest2 >= 1.0.0 python2-traceback2
%{?python_provide:%python_provide python2-testtools}

%description -n python2-testtools
Testtools is a set of extensions to the Python standard library's unit testing framework. These
extensions have been derived from years of experience with unit testing in Python and come from
many different sources.

%package -n python3-testtools
Summary:        Extensions to the Python unit testing framework
Requires:       python3-extras python3-mimeparse python3-pbr python3-unittest2 >= 1.0.0 python3-traceback2

%description -n python3-testtools
Testtools is a set of extensions to the Python standard library's unit testing framework. These
extensions have been derived from years of experience with unit testing in Python and come from
many different sources.

%package help
Summary:        Documentation for python-testtools
Requires:       python2-testtools = %{version}-%{release}
Provides:       bundled(jquery) %{name}-doc = %{version}-%{release}
Obsoletes:      %{name}-doc < %{version}-%{release}

%description help
This package contains HTML documentation for python-testtools.

%prep
%setup -q -n testtools-%{version}
%patch0002 -p1
rm -rf %{py3dir}
cp -a . %{py3dir}
cd %{py3dir}
%patch0001 -p1
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
rm -f %{py3dir}/testtools/_compat2x.py %{_builddir}/testtools-%{version}/testtools/_compat3x.py

%build
%{__python2} setup.py build
PYTHONPATH=$PWD make -C doc html
cd %{py3dir}
%{__python3} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
cd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%check
make PYTHON=%{__python2} check
cd %{py3dir}
make PYTHON=%{__python3} check

%files -n python2-testtools
%doc LICENSE NEWS README.rst
%{python2_sitelib}/*

%files -n python3-testtools
%doc LICENSE NEWS README.rst
%{python3_sitelib}/*

%files help
%doc doc/_build/html/*

%changelog
* Wed Nov 27 2019 lingsheng <lingsheng@huawei.com> - 2.3.0-10
- Package init