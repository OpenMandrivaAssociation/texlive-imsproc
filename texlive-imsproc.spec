# revision 29803
# category Package
# catalog-ctan /macros/xetex/latex/imsproc
# catalog-date 2013-04-04 12:47:47 +0200
# catalog-license lppl1.3
# catalog-version 0.1
Name:		texlive-imsproc
Version:	0.1
Release:	6
Summary:	Typeset IMS conference proceedings
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/xetex/latex/imsproc
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/imsproc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/imsproc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class typesets papers for IMS (Iranian Mathematical
Society) conference proceedings. The class uses the XePersian
package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/xelatex/imsproc/imsproc.cls
%doc %{_texmfdistdir}/doc/xelatex/imsproc/README
%doc %{_texmfdistdir}/doc/xelatex/imsproc/logo.JPG
%doc %{_texmfdistdir}/doc/xelatex/imsproc/sample-imsproc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
