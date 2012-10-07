Summary:	LibreOffice dingbats font
Summary(pl.UTF-8):	Fonty OpenSymbol
Name:		fonts-TTF-OpenSymbol
Version:	3.6.1.2
Release:	2
Epoch:		1
License:	GPL/LGPL
Group:		Fonts
URL:		http://cgit.freedesktop.org/libreoffice/core/tree/extras/source/truetype/symbol
Source0:	http://cgit.freedesktop.org/libreoffice/core/plain/extras/source/truetype/symbol/opens___.ttf
# Source0-md5:	ee33af866b0074ef4fcded5a578d0e7f
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
cp -p %{SOURCE0} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_fontsdir}/TTF
cp -p opens___.ttf $RPM_BUILD_ROOT%{_fontsdir}/TTF

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%{_fontsdir}/TTF/*.ttf
