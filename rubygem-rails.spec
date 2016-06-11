#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-rails
Version  : 4.2.6
Release  : 10
URL      : https://rubygems.org/downloads/rails-4.2.6.gem
Source0  : https://rubygems.org/downloads/rails-4.2.6.gem
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
%setup -q -D -T -n rails-4.2.6
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
rails-4.2.6.gem

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
/usr/lib64/ruby/gems/2.3.0/cache/rails-4.2.6.gem
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/README.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/CHANGELOG.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/akshaysurve.jpg
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/belongs_to.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/book_icon.gif
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/bullet.gif
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/chapters_icon.gif
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/check_bullet.gif
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/credits_pic_blank.gif
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/csrf.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/edge_badge.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/favicon.ico
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/feature_tile.gif
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/footer_tile.gif
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/fxn.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/getting_started/article_with_comments.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/getting_started/challenge.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/getting_started/confirm_dialog.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/getting_started/forbidden_attributes_for_new_article.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/getting_started/form_with_errors.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/getting_started/index_action_with_edit_link.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/getting_started/new_article.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/getting_started/rails_welcome.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/getting_started/routing_error_no_controller.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/getting_started/routing_error_no_route_matches.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/getting_started/show_action_for_articles.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/getting_started/template_is_missing_articles_new.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/getting_started/unknown_action_create_for_articles.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/getting_started/unknown_action_new_for_articles.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/grey_bullet.gif
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/habtm.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/has_many.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/has_many_through.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/has_one.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/has_one_through.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/header_backdrop.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/header_tile.gif
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/i18n/demo_html_safe.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/i18n/demo_localized_pirate.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/i18n/demo_translated_en.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/i18n/demo_translated_pirate.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/i18n/demo_translation_missing.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/i18n/demo_untranslated.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/icons/README
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/icons/callouts/1.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/icons/callouts/10.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/icons/callouts/11.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/icons/callouts/12.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/icons/callouts/13.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/icons/callouts/14.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/icons/callouts/15.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/icons/callouts/2.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/icons/callouts/3.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/icons/callouts/4.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/icons/callouts/5.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/icons/callouts/6.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/icons/callouts/7.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/icons/callouts/8.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/icons/callouts/9.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/icons/caution.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/icons/example.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/icons/home.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/icons/important.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/icons/next.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/icons/note.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/icons/prev.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/icons/tip.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/icons/up.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/icons/warning.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/nav_arrow.gif
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/oscardelben.jpg
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/polymorphic.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/radar.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/rails4_features.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/rails_guides_kindle_cover.jpg
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/rails_guides_logo.gif
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/rails_logo_remix.gif
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/session_fixation.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/tab_grey.gif
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/tab_info.gif
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/tab_note.gif
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/tab_red.gif
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/tab_yellow.gif
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/tab_yellow.png
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/images/vijaydev.jpg
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/javascripts/guides.js
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/javascripts/jquery.min.js
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/javascripts/responsive-tables.js
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/javascripts/syntaxhighlighter/shBrushAS3.js
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/javascripts/syntaxhighlighter/shBrushAppleScript.js
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/javascripts/syntaxhighlighter/shBrushBash.js
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/javascripts/syntaxhighlighter/shBrushCSharp.js
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/javascripts/syntaxhighlighter/shBrushColdFusion.js
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/javascripts/syntaxhighlighter/shBrushCpp.js
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/javascripts/syntaxhighlighter/shBrushCss.js
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/javascripts/syntaxhighlighter/shBrushDelphi.js
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/javascripts/syntaxhighlighter/shBrushDiff.js
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/javascripts/syntaxhighlighter/shBrushErlang.js
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/javascripts/syntaxhighlighter/shBrushGroovy.js
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/javascripts/syntaxhighlighter/shBrushJScript.js
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/javascripts/syntaxhighlighter/shBrushJava.js
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/javascripts/syntaxhighlighter/shBrushJavaFX.js
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/javascripts/syntaxhighlighter/shBrushPerl.js
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/javascripts/syntaxhighlighter/shBrushPhp.js
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/javascripts/syntaxhighlighter/shBrushPlain.js
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/javascripts/syntaxhighlighter/shBrushPowerShell.js
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/javascripts/syntaxhighlighter/shBrushPython.js
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/javascripts/syntaxhighlighter/shBrushRuby.js
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/javascripts/syntaxhighlighter/shBrushSass.js
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/javascripts/syntaxhighlighter/shBrushScala.js
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/javascripts/syntaxhighlighter/shBrushSql.js
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/javascripts/syntaxhighlighter/shBrushVb.js
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/javascripts/syntaxhighlighter/shBrushXml.js
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/javascripts/syntaxhighlighter/shCore.js
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/stylesheets/fixes.css
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/stylesheets/kindle.css
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/stylesheets/main.css
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/stylesheets/print.css
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/stylesheets/reset.css
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/stylesheets/responsive-tables.css
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/stylesheets/style.css
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/stylesheets/syntaxhighlighter/shCore.css
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/stylesheets/syntaxhighlighter/shCoreDefault.css
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/stylesheets/syntaxhighlighter/shCoreDjango.css
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/stylesheets/syntaxhighlighter/shCoreEclipse.css
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/stylesheets/syntaxhighlighter/shCoreEmacs.css
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/stylesheets/syntaxhighlighter/shCoreFadeToGrey.css
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/stylesheets/syntaxhighlighter/shCoreMDUltra.css
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/stylesheets/syntaxhighlighter/shCoreMidnight.css
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/stylesheets/syntaxhighlighter/shCoreRDark.css
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/stylesheets/syntaxhighlighter/shThemeDefault.css
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/stylesheets/syntaxhighlighter/shThemeDjango.css
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/stylesheets/syntaxhighlighter/shThemeEclipse.css
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/stylesheets/syntaxhighlighter/shThemeEmacs.css
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/stylesheets/syntaxhighlighter/shThemeFadeToGrey.css
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/stylesheets/syntaxhighlighter/shThemeMDUltra.css
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/stylesheets/syntaxhighlighter/shThemeMidnight.css
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/stylesheets/syntaxhighlighter/shThemeRDark.css
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/assets/stylesheets/syntaxhighlighter/shThemeRailsGuides.css
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/bug_report_templates/action_controller_gem.rb
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/bug_report_templates/action_controller_master.rb
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/bug_report_templates/active_record_gem.rb
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/bug_report_templates/active_record_master.rb
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/bug_report_templates/generic_gem.rb
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/bug_report_templates/generic_master.rb
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/rails_guides.rb
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/rails_guides/generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/rails_guides/helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/rails_guides/indexer.rb
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/rails_guides/kindle.rb
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/rails_guides/levenshtein.rb
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/rails_guides/markdown.rb
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/rails_guides/markdown/renderer.rb
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/2_2_release_notes.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/2_3_release_notes.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/3_0_release_notes.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/3_1_release_notes.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/3_2_release_notes.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/4_0_release_notes.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/4_1_release_notes.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/4_2_release_notes.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/_license.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/_welcome.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/action_controller_overview.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/action_mailer_basics.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/action_view_overview.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/active_job_basics.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/active_model_basics.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/active_record_basics.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/active_record_callbacks.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/active_record_migrations.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/active_record_postgresql.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/active_record_querying.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/active_record_validations.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/active_support_core_extensions.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/active_support_instrumentation.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/api_documentation_guidelines.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/asset_pipeline.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/association_basics.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/autoloading_and_reloading_constants.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/caching_with_rails.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/command_line.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/configuring.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/contributing_to_ruby_on_rails.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/credits.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/debugging_rails_applications.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/development_dependencies_install.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/documents.yaml
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/engines.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/form_helpers.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/generators.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/getting_started.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/i18n.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/index.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/initialization.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/kindle/copyright.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/kindle/layout.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/kindle/rails_guides.opf.erb
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/kindle/toc.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/kindle/toc.ncx.erb
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/kindle/welcome.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/layout.html.erb
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/layouts_and_rendering.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/maintenance_policy.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/nested_model_forms.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/plugins.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/rails_application_templates.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/rails_on_rack.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/routing.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/ruby_on_rails_guides_guidelines.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/security.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/testing.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/upgrading_ruby_on_rails.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/source/working_with_javascript_in_rails.md
/usr/lib64/ruby/gems/2.3.0/gems/rails-4.2.6/guides/w3c_validator.rb
/usr/lib64/ruby/gems/2.3.0/specifications/rails-4.2.6.gemspec
