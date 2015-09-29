#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-rails
Version  : 4.2.3
Release  : 7
URL      : https://rubygems.org/downloads/rails-4.2.3.gem
Source0  : https://rubygems.org/downloads/rails-4.2.3.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-sprockets-rails

%description
Replaced the plain DocBook XSL admonition icons with Jimmac's DocBook
icons (http://jimmac.musichall.cz/ikony.php3). I dropped transparency
from the Jimmac icons to get round MS IE and FOP PNG incompatibilities.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n rails-4.2.3
gem spec %{SOURCE0} -l --ruby > rubygem-rails.gemspec

%build
gem build rubygem-rails.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
rails-4.2.3.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/rails-4.2.3.gem
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/ActiveRecord/cdesc-ActiveRecord.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/BugTest/app-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/BugTest/cdesc-BugTest.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/BugTest/test_association_stuff-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/BugTest/test_returns_success-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/BugTest/test_stuff-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/Comment/cdesc-Comment.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/Kindle/add_head_section-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/Kindle/cdesc-Kindle.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/Kindle/generate-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/Kindle/generate_document_metadata-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/Kindle/generate_front_matter-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/Kindle/generate_sections-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/Minitest/cdesc-Minitest.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/Object/bundler%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/Object/cdesc-Object.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/Post/cdesc-Post.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Generator/all-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Generator/cdesc-Generator.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Generator/check_for_kindlegen-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Generator/check_fragment_identifiers-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Generator/copy_assets-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Generator/create_output_dir_if_needed-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Generator/edge-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Generator/extract_anchors-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Generator/generate%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Generator/generate-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Generator/generate_guide-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Generator/generate_guides-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Generator/generate_mobi-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Generator/guides_dir-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Generator/guides_to_generate-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Generator/initialize_dirs-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Generator/kindle%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Generator/mobi-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Generator/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Generator/output_dir-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Generator/output_file_for-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Generator/output_path_for-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Generator/register_kindle_mime_types-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Generator/select_only-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Generator/set_flags_from_environment-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Generator/source_dir-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Generator/warn_about_broken_links-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Generator/warnings-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Helpers/author-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Helpers/cdesc-Helpers.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Helpers/code-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Helpers/docs_for_menu-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Helpers/documents_by_section-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Helpers/documents_flat-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Helpers/finished_documents-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Helpers/guide-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Indexer/body-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Indexer/cdesc-Indexer.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Indexer/index-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Indexer/level_hash-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Indexer/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Indexer/process-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Indexer/result-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Indexer/title_to_idx-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Indexer/warnings-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Levenshtein/cdesc-Levenshtein.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Levenshtein/distance-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Markdown/Renderer/block_code-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Markdown/Renderer/brush_for-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Markdown/Renderer/cdesc-Renderer.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Markdown/Renderer/convert_footnotes-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Markdown/Renderer/convert_notes-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Markdown/Renderer/header-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Markdown/Renderer/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Markdown/Renderer/paragraph-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Markdown/cdesc-Markdown.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Markdown/dom_id-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Markdown/dom_id_text-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Markdown/engine-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Markdown/extract_raw_header_and_body-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Markdown/generate_body-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Markdown/generate_header-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Markdown/generate_index-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Markdown/generate_structure-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Markdown/generate_title-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Markdown/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Markdown/node_index-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Markdown/render-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Markdown/render_page-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Validator/cdesc-Validator.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Validator/guides_to_validate-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Validator/select_only-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Validator/show_results-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/Validator/validate-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/RailsGuides/cdesc-RailsGuides.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/TestApp/cdesc-TestApp.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/TestController/cdesc-TestController.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/TestController/index-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/images/icons/page-README.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/javascripts/page-guides_js.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/javascripts/page-jquery_min_js.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/javascripts/page-responsive-tables_js.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/javascripts/syntaxhighlighter/page-shBrushAS3_js.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/javascripts/syntaxhighlighter/page-shBrushAppleScript_js.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/javascripts/syntaxhighlighter/page-shBrushBash_js.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/javascripts/syntaxhighlighter/page-shBrushCSharp_js.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/javascripts/syntaxhighlighter/page-shBrushColdFusion_js.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/javascripts/syntaxhighlighter/page-shBrushCpp_js.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/javascripts/syntaxhighlighter/page-shBrushCss_js.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/javascripts/syntaxhighlighter/page-shBrushDelphi_js.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/javascripts/syntaxhighlighter/page-shBrushDiff_js.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/javascripts/syntaxhighlighter/page-shBrushErlang_js.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/javascripts/syntaxhighlighter/page-shBrushGroovy_js.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/javascripts/syntaxhighlighter/page-shBrushJScript_js.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/javascripts/syntaxhighlighter/page-shBrushJavaFX_js.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/javascripts/syntaxhighlighter/page-shBrushJava_js.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/javascripts/syntaxhighlighter/page-shBrushPerl_js.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/javascripts/syntaxhighlighter/page-shBrushPhp_js.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/javascripts/syntaxhighlighter/page-shBrushPlain_js.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/javascripts/syntaxhighlighter/page-shBrushPowerShell_js.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/javascripts/syntaxhighlighter/page-shBrushPython_js.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/javascripts/syntaxhighlighter/page-shBrushRuby_js.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/javascripts/syntaxhighlighter/page-shBrushSass_js.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/javascripts/syntaxhighlighter/page-shBrushScala_js.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/javascripts/syntaxhighlighter/page-shBrushSql_js.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/javascripts/syntaxhighlighter/page-shBrushVb_js.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/javascripts/syntaxhighlighter/page-shBrushXml_js.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/javascripts/syntaxhighlighter/page-shCore_js.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/stylesheets/page-fixes_css.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/stylesheets/page-kindle_css.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/stylesheets/page-main_css.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/stylesheets/page-print_css.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/stylesheets/page-reset_css.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/stylesheets/page-responsive-tables_css.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/stylesheets/page-style_css.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/stylesheets/syntaxhighlighter/page-shCoreDefault_css.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/stylesheets/syntaxhighlighter/page-shCoreDjango_css.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/stylesheets/syntaxhighlighter/page-shCoreEclipse_css.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/stylesheets/syntaxhighlighter/page-shCoreEmacs_css.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/stylesheets/syntaxhighlighter/page-shCoreFadeToGrey_css.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/stylesheets/syntaxhighlighter/page-shCoreMDUltra_css.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/stylesheets/syntaxhighlighter/page-shCoreMidnight_css.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/stylesheets/syntaxhighlighter/page-shCoreRDark_css.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/stylesheets/syntaxhighlighter/page-shCore_css.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/stylesheets/syntaxhighlighter/page-shThemeDefault_css.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/stylesheets/syntaxhighlighter/page-shThemeDjango_css.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/stylesheets/syntaxhighlighter/page-shThemeEclipse_css.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/stylesheets/syntaxhighlighter/page-shThemeEmacs_css.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/stylesheets/syntaxhighlighter/page-shThemeFadeToGrey_css.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/stylesheets/syntaxhighlighter/page-shThemeMDUltra_css.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/stylesheets/syntaxhighlighter/page-shThemeMidnight_css.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/stylesheets/syntaxhighlighter/page-shThemeRDark_css.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/assets/stylesheets/syntaxhighlighter/page-shThemeRailsGuides_css.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/page-CHANGELOG_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/page-Rakefile.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-2_2_release_notes_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-2_3_release_notes_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-3_0_release_notes_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-3_1_release_notes_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-3_2_release_notes_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-4_0_release_notes_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-4_1_release_notes_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-4_2_release_notes_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-action_controller_overview_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-action_mailer_basics_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-action_view_overview_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-active_job_basics_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-active_model_basics_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-active_record_basics_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-active_record_callbacks_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-active_record_migrations_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-active_record_postgresql_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-active_record_querying_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-active_record_validations_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-active_support_core_extensions_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-active_support_instrumentation_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-api_documentation_guidelines_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-asset_pipeline_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-association_basics_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-autoloading_and_reloading_constants_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-caching_with_rails_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-command_line_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-configuring_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-contributing_to_ruby_on_rails_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-debugging_rails_applications_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-development_dependencies_install_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-documents_yaml.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-engines_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-form_helpers_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-generators_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-getting_started_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-i18n_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-initialization_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-layouts_and_rendering_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-maintenance_policy_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-nested_model_forms_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-plugins_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-rails_application_templates_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-rails_on_rack_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-routing_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-ruby_on_rails_guides_guidelines_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-security_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-testing_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-upgrading_ruby_on_rails_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/guides/source/page-working_with_javascript_in_rails_md.ri
/usr/lib64/ruby/gems/2.2.0/doc/rails-4.2.3/ri/page-README_md.ri
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/README.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/CHANGELOG.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/akshaysurve.jpg
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/belongs_to.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/book_icon.gif
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/bullet.gif
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/chapters_icon.gif
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/check_bullet.gif
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/credits_pic_blank.gif
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/csrf.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/edge_badge.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/favicon.ico
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/feature_tile.gif
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/footer_tile.gif
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/fxn.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/getting_started/article_with_comments.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/getting_started/challenge.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/getting_started/confirm_dialog.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/getting_started/forbidden_attributes_for_new_article.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/getting_started/form_with_errors.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/getting_started/index_action_with_edit_link.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/getting_started/new_article.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/getting_started/rails_welcome.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/getting_started/routing_error_no_controller.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/getting_started/routing_error_no_route_matches.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/getting_started/show_action_for_articles.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/getting_started/template_is_missing_articles_new.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/getting_started/unknown_action_create_for_articles.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/getting_started/unknown_action_new_for_articles.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/grey_bullet.gif
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/habtm.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/has_many.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/has_many_through.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/has_one.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/has_one_through.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/header_backdrop.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/header_tile.gif
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/i18n/demo_html_safe.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/i18n/demo_localized_pirate.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/i18n/demo_translated_en.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/i18n/demo_translated_pirate.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/i18n/demo_translation_missing.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/i18n/demo_untranslated.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/icons/README
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/icons/callouts/1.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/icons/callouts/10.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/icons/callouts/11.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/icons/callouts/12.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/icons/callouts/13.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/icons/callouts/14.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/icons/callouts/15.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/icons/callouts/2.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/icons/callouts/3.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/icons/callouts/4.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/icons/callouts/5.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/icons/callouts/6.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/icons/callouts/7.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/icons/callouts/8.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/icons/callouts/9.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/icons/caution.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/icons/example.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/icons/home.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/icons/important.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/icons/next.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/icons/note.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/icons/prev.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/icons/tip.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/icons/up.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/icons/warning.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/nav_arrow.gif
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/oscardelben.jpg
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/polymorphic.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/radar.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/rails4_features.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/rails_guides_kindle_cover.jpg
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/rails_guides_logo.gif
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/rails_logo_remix.gif
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/session_fixation.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/tab_grey.gif
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/tab_info.gif
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/tab_note.gif
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/tab_red.gif
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/tab_yellow.gif
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/tab_yellow.png
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/images/vijaydev.jpg
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/javascripts/guides.js
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/javascripts/jquery.min.js
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/javascripts/responsive-tables.js
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/javascripts/syntaxhighlighter/shBrushAS3.js
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/javascripts/syntaxhighlighter/shBrushAppleScript.js
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/javascripts/syntaxhighlighter/shBrushBash.js
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/javascripts/syntaxhighlighter/shBrushCSharp.js
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/javascripts/syntaxhighlighter/shBrushColdFusion.js
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/javascripts/syntaxhighlighter/shBrushCpp.js
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/javascripts/syntaxhighlighter/shBrushCss.js
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/javascripts/syntaxhighlighter/shBrushDelphi.js
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/javascripts/syntaxhighlighter/shBrushDiff.js
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/javascripts/syntaxhighlighter/shBrushErlang.js
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/javascripts/syntaxhighlighter/shBrushGroovy.js
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/javascripts/syntaxhighlighter/shBrushJScript.js
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/javascripts/syntaxhighlighter/shBrushJava.js
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/javascripts/syntaxhighlighter/shBrushJavaFX.js
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/javascripts/syntaxhighlighter/shBrushPerl.js
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/javascripts/syntaxhighlighter/shBrushPhp.js
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/javascripts/syntaxhighlighter/shBrushPlain.js
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/javascripts/syntaxhighlighter/shBrushPowerShell.js
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/javascripts/syntaxhighlighter/shBrushPython.js
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/javascripts/syntaxhighlighter/shBrushRuby.js
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/javascripts/syntaxhighlighter/shBrushSass.js
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/javascripts/syntaxhighlighter/shBrushScala.js
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/javascripts/syntaxhighlighter/shBrushSql.js
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/javascripts/syntaxhighlighter/shBrushVb.js
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/javascripts/syntaxhighlighter/shBrushXml.js
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/javascripts/syntaxhighlighter/shCore.js
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/stylesheets/fixes.css
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/stylesheets/kindle.css
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/stylesheets/main.css
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/stylesheets/print.css
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/stylesheets/reset.css
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/stylesheets/responsive-tables.css
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/stylesheets/style.css
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/stylesheets/syntaxhighlighter/shCore.css
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/stylesheets/syntaxhighlighter/shCoreDefault.css
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/stylesheets/syntaxhighlighter/shCoreDjango.css
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/stylesheets/syntaxhighlighter/shCoreEclipse.css
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/stylesheets/syntaxhighlighter/shCoreEmacs.css
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/stylesheets/syntaxhighlighter/shCoreFadeToGrey.css
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/stylesheets/syntaxhighlighter/shCoreMDUltra.css
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/stylesheets/syntaxhighlighter/shCoreMidnight.css
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/stylesheets/syntaxhighlighter/shCoreRDark.css
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/stylesheets/syntaxhighlighter/shThemeDefault.css
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/stylesheets/syntaxhighlighter/shThemeDjango.css
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/stylesheets/syntaxhighlighter/shThemeEclipse.css
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/stylesheets/syntaxhighlighter/shThemeEmacs.css
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/stylesheets/syntaxhighlighter/shThemeFadeToGrey.css
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/stylesheets/syntaxhighlighter/shThemeMDUltra.css
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/stylesheets/syntaxhighlighter/shThemeMidnight.css
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/stylesheets/syntaxhighlighter/shThemeRDark.css
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/assets/stylesheets/syntaxhighlighter/shThemeRailsGuides.css
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/bug_report_templates/action_controller_gem.rb
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/bug_report_templates/action_controller_master.rb
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/bug_report_templates/active_record_gem.rb
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/bug_report_templates/active_record_master.rb
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/bug_report_templates/generic_gem.rb
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/bug_report_templates/generic_master.rb
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/rails_guides.rb
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/rails_guides/generator.rb
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/rails_guides/helpers.rb
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/rails_guides/indexer.rb
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/rails_guides/kindle.rb
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/rails_guides/levenshtein.rb
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/rails_guides/markdown.rb
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/rails_guides/markdown/renderer.rb
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/2_2_release_notes.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/2_3_release_notes.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/3_0_release_notes.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/3_1_release_notes.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/3_2_release_notes.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/4_0_release_notes.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/4_1_release_notes.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/4_2_release_notes.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/_license.html.erb
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/_welcome.html.erb
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/action_controller_overview.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/action_mailer_basics.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/action_view_overview.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/active_job_basics.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/active_model_basics.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/active_record_basics.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/active_record_callbacks.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/active_record_migrations.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/active_record_postgresql.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/active_record_querying.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/active_record_validations.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/active_support_core_extensions.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/active_support_instrumentation.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/api_documentation_guidelines.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/asset_pipeline.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/association_basics.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/autoloading_and_reloading_constants.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/caching_with_rails.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/command_line.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/configuring.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/contributing_to_ruby_on_rails.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/credits.html.erb
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/debugging_rails_applications.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/development_dependencies_install.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/documents.yaml
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/engines.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/form_helpers.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/generators.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/getting_started.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/i18n.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/index.html.erb
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/initialization.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/kindle/copyright.html.erb
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/kindle/layout.html.erb
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/kindle/rails_guides.opf.erb
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/kindle/toc.html.erb
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/kindle/toc.ncx.erb
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/kindle/welcome.html.erb
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/layout.html.erb
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/layouts_and_rendering.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/maintenance_policy.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/nested_model_forms.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/plugins.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/rails_application_templates.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/rails_on_rack.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/routing.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/ruby_on_rails_guides_guidelines.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/security.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/testing.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/upgrading_ruby_on_rails.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/source/working_with_javascript_in_rails.md
/usr/lib64/ruby/gems/2.2.0/gems/rails-4.2.3/guides/w3c_validator.rb
/usr/lib64/ruby/gems/2.2.0/specifications/rails-4.2.3.gemspec
