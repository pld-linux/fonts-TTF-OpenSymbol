Summary:	LibreOffice dingbats font
Summary(pl.UTF-8):	Fonty OpenSymbol
Name:		fonts-TTF-OpenSymbol
Version:	3.6.1.2
Release:	1
Epoch:		1
License:	GPL/LGPL
Group:		Fonts
URL:		http://www.openoffice.org/
# TODO: find direct link to their VCS for smaller src.rpm
Source0:	http://download.documentfoundation.org/libreoffice/src/3.6.1/libreoffice-core-%{version}.tar.xz
# Source0-md5:	3ddcf145b74daa4361e48dafe97e7d21
Requires(post,postun):	fontpostinst
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	openoffice.org-fonts-OpenSymbol
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A dingbats font, OpenSymbol, suitable for use by LibreOffice for
bullets and mathematical symbols.

%description  -l pl.UTF-8
Fonty TrueType OpenSymbol.

%prep
%setup -qcT
DN=$(basename %{SOURCE0} .tar.xz)
%{__tar} -Jxf %{SOURCE0} $DN/extras/source/truetype/symbol
mv $DN/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_fontsdir}/TTF
cp -p extras/source/truetype/symbol/opens___.ttf $RPM_BUILD_ROOT%{_fontsdir}/TTF

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%{_fontsdir}/TTF/*.ttf
