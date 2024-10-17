Name:		texlive-imsproc
Version:	29803
Release:	2
Summary:	Typeset IMS conference proceedings
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/imsproc
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/imsproc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/imsproc.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
