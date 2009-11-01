%define		upd			300
%define		mws			OOO%{upd}
%define		tag			%(echo %{mws} | tr A-Z a-z)-%{milestone}
%define		milestone	m15
%define		_tag		%(echo %{tag} | tr - _)
%define		rel	10
Summary:	OpenSymbol fonts
Summary(pl.UTF-8):	Fonty OpenSymbol
Name:		fonts-TTF-OpenSymbol
Version:	3.0.1.3
# use rel "1" when version increased
Release:	%{_tag}.%{rel}
Epoch:		1
License:	GPL/LGPL
Group:		Fonts
URL:		http://www.openoffice.org/
Source0:	http://download.go-oo.org/%{mws}/%{tag}-l10n.tar.bz2
# Source0-md5:	02b20bd978e342de45ef84d3232e3f94
Requires(post,postun):	fontpostinst
Obsoletes:	openoffice.org-fonts-OpenSymbol
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenSymbol TrueType fonts.

%description  -l pl.UTF-8
Fonty TrueType OpenSymbol.

%prep
%setup -qc
mv ooo*-*-l10n/* .

%install
# Copy fixed OpenSymbol to correct location
install -d $RPM_BUILD_ROOT%{_fontsdir}/TTF
cp -a extras/source/truetype/symbol/opens___.ttf $RPM_BUILD_ROOT%{_fontsdir}/TTF

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%{_fontsdir}/TTF/*.ttf
