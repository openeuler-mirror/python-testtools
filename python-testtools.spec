Name:           python-testtools
Version:        2.4.0
Release:        1
Summary:        Extensions to the Python unit testing framework
License:        MIT
URL:            https://launchpad.net/testtools

Source0:        https://pypi.io/packages/source/t/testtools/testtools-%{version}.tar.gz
BuildRequires:  python3-extras python3-mimeparse python3-pbr python3-setuptools python3-unittest2
BuildRequires:  python3-traceback2 python3-testscenarios python3-sphinx python3-devel
BuildArch:      noarch
Patch0:         testtools-2.4.0-fix-py3-compat.patch

%description
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
Requires:       python3-testtools = %{version}-%{release}
Provides:       bundled(jquery) %{name}-doc = %{version}-%{release}
Obsoletes:      %{name}-doc < %{version}-%{release}

%description help
This package contains HTML documentation for python-testtools.

%prep
%autosetup -n testtools-%{version} -p1
rm -rf testtools.egg-info

%build
%py3_build
PYTHONPATH=$PWD make -C doc html

%install
%py3_install

%check
make PYTHON=%{__python3} check

%files -n python3-testtools
%doc LICENSE NEWS README.rst
%{python3_sitelib}/*

%files help
%doc doc/_build/html/*

%changelog
* Fri Aug 06 2021 liusheng <liusheng2048@gmail.com> - 2.4.0-1
- Upgrade to version 2.4.0

* Tue Aug 11 2020 zhangtao <zhangtao221@huawei.com> - 2.3.0-12
- Del Python2-testtools python2 is EOL and we recommend python3

* Thu Feb 20 2020 lingsheng <lingsheng@huawei.com> - 2.3.0-11
- Modify buildrequires to fix build fail

* Wed Nov 27 2019 lingsheng <lingsheng@huawei.com> - 2.3.0-10
- Package init
