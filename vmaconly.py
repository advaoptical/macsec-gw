<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>
    pqc/mce Files
        &middot; vmaconly.py

        &middot; APT Repository
</title>
        <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
        <meta name="robots" content="index, nofollow"/>
        <link rel="icon" href="/repo/images/favicon.ico" type="image/png" />

        

        

        
            <link rel="stylesheet" type="text/css" href="/repo/css/fontawesome_extension.css" media="screen"/>
            <link rel="stylesheet" type="text/css" href="/repo/css/fontawesome.css" media="screen"/>
            <link rel="stylesheet" type="text/css" href="/repo/js/select2/select2.css?ver=2.1.0"/>
            <link rel="stylesheet" type="text/css" href="/repo/css/pygments.css?ver=2.1.0"/>
            <link rel="stylesheet" type="text/css" href="/repo/css/newstyle.css?ver=2.1.0" media="screen"/>
            <link rel="stylesheet" type="text/css" href="/repo/css/bootstrap.css?ver=2.1.0" media="screen"/>
            
        


        
        
        
            <script type="text/javascript">
            //JS translations map
            var TRANSLATION_MAP = {
                'Add another comment':'Add another comment',
                'Stop following this repository':"Stop following this repository",
                'Start following this repository':"Start following this repository",
                'Group':"Group",
                'members':"members",
                'Loading ...':"Loading ...",
                'loading ...':"loading ...",
                'Search truncated': "Search truncated",
                'No matching files': "No matching files",
                'Open new pull request': "Open new pull request",
                'Open new pull request for selected changesets':  "Open new pull request for selected changesets",
                'Show selected changesets __S -> __E': "Show selected changesets __S -&gt; __E",
                'Show selected changeset __S': "Show selected changeset __S",
                'Selection link': "Selection link",
                'Collapse diff': "Collapse diff",
                'Expand diff': "Expand diff",
                'Failed to revoke permission': "Failed to revoke permission",
                'Confirm to revoke permission for {0}: {1} ?': "confirm to revoke permission for {0}: {1} ?",
                'enabled': "enabled",
                'disabled': "disabled",
                'Select changeset': "Select changeset",
                'specify changeset': "specify changeset",
                'MSG_SORTASC': "Click to sort ascending",
                'MSG_SORTDESC': "Click to sort descending",
                'MSG_EMPTY': "No records found.",
                'MSG_ERROR': "Data error.",
                'MSG_LOADING': "Loading...",


            };
            var _TM = TRANSLATION_MAP;

            var TOGGLE_FOLLOW_URL  = "/repo/_admin/toggle_following";

            var REPO_NAME = "";
                var REPO_NAME = "pqc/mce";
            </script>
            <script type="text/javascript" src="/repo/js/yui.2.9.js?ver=2.1.0"></script>
            <script type="text/javascript" src="/repo/js/jquery-1.10.2.min.js?ver=2.1.0"></script>
            <script type="text/javascript" src="/repo/js/bootstrap.js?ver=2.1.0"></script>
            <script type="text/javascript" src="/repo/js/select2/select2.js?ver=2.1.0"></script>
            <script type="text/javascript" src="/repo/js/mousetrap.js?ver=2.1.0"></script>
            <!--[if lt IE 9]>
               <script language="javascript" type="text/javascript" src="/repo/js/excanvas.min.js"></script>
            <![endif]-->
            <script type="text/javascript" src="/repo/js/yui.flot.js?ver=2.1.0"></script>
            <script type="text/javascript" src="/repo/js/native.history.js?ver=2.1.0"></script>
            <script type="text/javascript" src="/repo/js/pyroutes_map.js?ver=2.1.0"></script>
            <script type="text/javascript" src="/repo/js/rhodecode.js?ver=2.1.0"></script>
           
            <script type="text/javascript">
            (function(window,undefined){
                // Prepare
                var History = window.History; // Note: We are using a capital H instead of a lower h
                if ( !History.enabled ) {
                     // History.js is disabled for this browser.
                     // This is because we can optionally choose to support HTML4 browsers or not.
                    return false;
                }
            })(window);

            YUE.onDOMReady(function(){
              tooltip_activate();
              show_more_event();
              show_changeset_tooltip();
              // routes registration
              pyroutes.register('home', "/repo/", []);
              pyroutes.register('new_gist', "/repo/_admin/gists/new", []);
              pyroutes.register('new_repo', "/repo/_admin/create_repository", []);

              pyroutes.register('summary_home', "/repo/%25%28repo_name%29s", ['repo_name']);
              pyroutes.register('changelog_home', "/repo/%25%28repo_name%29s/changelog", ['repo_name']);
              pyroutes.register('files_home', "/repo/%25%28repo_name%29s/files/%25%28revision%29s/%25%28f_path%29s", ['repo_name', 'revision', 'f_path']);
              pyroutes.register('edit_repo', "/repo/%25%28repo_name%29s/settings", ['repo_name']);
              pyroutes.register('pullrequest_home', "/repo/%25%28repo_name%29s/pull-request/new", ['repo_name']);

              pyroutes.register('toggle_following', "/repo/_admin/toggle_following");
              pyroutes.register('changeset_info', "/repo/changeset_info/%25%28repo_name%29s/%25%28revision%29s", ['repo_name', 'revision']);
              pyroutes.register('repo_size', "/repo/%25%28repo_name%29s/repo_size", ['repo_name']);
              pyroutes.register('changeset_comment_preview', "/repo/%25%28repo_name%29s/changeset/comment/preview", ['repo_name']);
              pyroutes.register('repo_refs_data', "/repo/%25%28repo_name%29s/refs-data", ['repo_name']);
           })
            </script>
        
        
        
    </head>
    <body id="body">
      <!--[if IE 7]>
      <script>YUD.addClass(document.body,'ie7')</script>
      <![endif]-->
      <!--[if IE 8]>
      <script>YUD.addClass(document.body,'ie8')</script>
      <![endif]-->
      <!--[if IE 9]>
      <script>YUD.addClass(document.body,'ie9')</script>
      <![endif]-->

      

<!-- HEADER -->
<div id="header">
    <div id="header-inner" class="title">
        <div id="logo">
            <div class="header">
                <a href="/repo/"><img src="/repo/images/rhodecode-logo-white-216x60.png" alt="RhodeCode"/></a>
            </div>
             <div class="branding">- APT Repository</div>
        </div>
        <!-- MENU -->
        
    
        
        <ul id="quick" class="horizontal-list">
          <!-- repo switcher -->
          <li class="current">
            <input id="repo_switcher" name="repo_switcher" type="hidden">
          </li>

            <li >
              <a class="menu_link" title="Public journal"  href="/repo/_admin/public_journal">
                <i class="icon-book"></i> Public journal
              </a>
            </li>
            <li >
              <a class="menu_link childs" title="Show public gists"  href="/repo/_admin/gists">
                <i class="icon-file-2"></i> Gists
              </a>
                <ul class="admin_menu">
                  <li><a href="/repo/_admin/gists/new?public=1"><i class="icon-file-alt"></i> Create new gist</a></li>
                  <li><a href="/repo/_admin/gists"><i class="icon-copy"></i> All public gists</a></li>
                </ul>
            </li>
          <li >
              <a class="menu_link" title="Search in repositories"  href="/repo/_admin/search">
                <i class="icon-search"></i> Search
              </a>
          </li>
          <li >
              <a class="menu_link childs" title="Admin">
                <i class="icon-cog"></i> Admin
              </a>
              
  <ul>
      <li><a href="/repo/_admin/repos"><i class="icon-archive"></i> Repositories</a></li>
      <li><a href="/repo/_admin/repo_groups"><i class="icon-folder-close"></i> Repository groups</a></li>
  </ul>

          </li>
          
    <li>
      <a class="menu_link childs" id="quick_login_link">
          <span class="icon">
             <img src="/repo/images/user20.png" alt="avatar">
          </span>
              <span>Not logged in</span>
      </a>

  <div class="user-menu">
      <div id="quick_login">
            <h4>Login to your account</h4>
            <form action="/repo/_admin/login?came_from=%2Frepo%2Fpqc%2Fmce%2Ffiles%2F97e2950099623bba7e79dab038df386cd774d48b%2Fvmaconly.py" method="post">
            <div class="form">
                <div class="fields">
                    <div class="field">
                        <div class="label">
                            <label for="username">Username:</label>
                        </div>
                        <div class="input">
                            <input class="focus" id="username" name="username" type="text" />
                        </div>

                    </div>
                    <div class="field">
                        <div class="label">
                            <label for="password">Password:</label>
                        </div>
                        <div class="input">
                            <input class="focus" id="password" name="password" type="password" />
                        </div>

                    </div>
                    <div class="buttons">
                        <div class="password_forgoten"><a href="/repo/_admin/password_reset">Forgot password ?</a></div>
                        <div class="register">
                         <a href="/repo/_admin/register">Don&#39;t have an account ?</a>
                        </div>
                        <div class="submit">
                            <input class="btn btn-mini" id="sign_in" name="sign_in" type="submit" value="Log In" />
                        </div>
                    </div>
                </div>
            </div>
            </form>
      </div>
  </div>

    </li>


    <script type="text/javascript">
        var visual_show_public_icon = "True" == "True";
        var cache = {}
        /*format the look of items in the list*/
        var format = function(state){
            if (!state.id){
              return state.text; // optgroup
            }
            var obj_dict = state.obj;
            var tmpl = '';

            if(obj_dict && state.type == 'repo'){
                if(obj_dict['repo_type'] === 'hg'){
                    tmpl += '<i class="icon-hg"></i> ';
                }
                else if(obj_dict['repo_type'] === 'git'){
                    tmpl += '<i class="icon-git"></i> ';
                }
                if(obj_dict['private']){
                    tmpl += '<i class="icon-lock" style="color: #e85634;"></i> ';
                }
                else if(visual_show_public_icon){
                    tmpl += '<i class="icon-unlock-alt"></i> ';
                }
            }
            if(obj_dict && state.type == 'group'){
                    tmpl += '<i class="icon-folder-close"></i> ';
            }
            tmpl += state.text;
            return tmpl;
        }

        $("#repo_switcher").select2({
            placeholder: '<i class="icon-archive"></i> Repositories <i class="icon-caret-down"></i>',
            dropdownAutoWidth: true,
            formatResult: format,
            formatSelection: format,
            formatNoMatches: function(term){
                return "No matches found";
            },
            containerCssClass: "repo-switcher",
            dropdownCssClass: "repo-switcher-dropdown",
            escapeMarkup: function(m){
                // don't escape our custom placeholder
                if(m.substr(0,28) == '<i class="icon-archive"></i>'){
                    return m;
                }

                return Select2.util.escapeMarkup(m);
            },
            query: function(query){
              var key = 'cache';
              var cached = cache[key] ;
              if(cached) {
                var data = {results: []};
                //filter results
                $.each(cached.results, function(){
                    var section = this.text;
                    var children = [];
                    $.each(this.children, function(){
                        if(query.term.length == 0 || this.text.toUpperCase().indexOf(query.term.toUpperCase()) >= 0 ){
                            children.push({'id': this.id, 'text': this.text, 'type': this.type, 'obj': this.obj})
                        }
                    })
                    if(children.length !== 0){
                        data.results.push({'text': section, 'children': children})
                    }

                });
                query.callback(data);
              }else{
                  $.ajax({
                    url: "/repo/_repos",
                    data: {},
                    dataType: 'json',
                    type: 'GET',
                    success: function(data) {
                      cache[key] = data;
                      query.callback({results: data.results});
                    }
                  })
              }
            },
        });

        $("#repo_switcher").on('select2-selecting', function(e){
            e.preventDefault();
            window.location = pyroutes.url('summary_home', {'repo_name': e.val})
        })


        // general help "?"
        Mousetrap.bind(['?'], function(e) {
            $('#help_kb').modal({})
        });

        // / open the quick filter
        Mousetrap.bind(['/'], function(e) {
            $("#repo_switcher").select2("open");

            // return false to prevent default browser behavior
            // and stop event from bubbling
            return false;
        });

        // ctrl/command+b, show the the main bar
        Mousetrap.bind(['command+b', 'ctrl+b'], function(e) {
            if($('#header-inner').hasClass('hover') && $('#content').hasClass('hover')){
                $('#header-inner').removeClass('hover');
                $('#content').removeClass('hover');
            }
            else{
                $('#header-inner').addClass('hover');
                $('#content').addClass('hover');
            }
            return false;
        });

        // general nav g + action
        Mousetrap.bind(['g h'], function(e) {
            window.location = pyroutes.url('home');
        });
        Mousetrap.bind(['n g'], function(e) {
            window.location = pyroutes.url('new_gist');
        });
        Mousetrap.bind(['n r'], function(e) {
            window.location = pyroutes.url('new_repo');
        });

            // nav in repo context
            Mousetrap.bind(['g s'], function(e) {
                window.location = pyroutes.url('summary_home', {'repo_name': REPO_NAME});
            });
            Mousetrap.bind(['g c'], function(e) {
                window.location = pyroutes.url('changelog_home', {'repo_name': REPO_NAME});
            });
            Mousetrap.bind(['g f'], function(e) {
                window.location = pyroutes.url('files_home', {'repo_name': REPO_NAME, 'revision': 'tip', 'f_path': ''});
            });
            Mousetrap.bind(['g o'], function(e) {
                window.location = pyroutes.url('edit_repo', {'repo_name': REPO_NAME});
            });

    </script>


        <!-- END MENU -->
        









    </div>
</div>
<!-- END HEADER -->

<!-- CONTENT -->
<div id="content">
    
    <div class="flash_msg">
    
    <script>
    if (typeof jQuery != 'undefined') {
        $(".alert").alert();
    }
    </script>
</div>


    <div id="main">
        

  
  

  <!--- CONTEXT BAR -->
  <div id="context-bar" class="box">
      <h2>
          <i class="icon-git" style="color: #e85634; font-size: 24px"></i>

          <i class="icon-unlock-alt"></i>
        <a href="/repo/pqc">pqc</a> &raquo; <span><a href="/repo/pqc/mce">mce</a></span>
      </h2>
      <!--
      <div id="breadcrumbs">
        <a href="/repo/">Repositories</a>
        &raquo;
        <a href="/repo/pqc">pqc</a> &raquo; <span><a href="/repo/pqc/mce">mce</a></span>
      </div>
      -->
      <ul id="context-pages" class="horizontal-list">
        <li ><a href="/repo/pqc/mce"><i class="icon-file-text"></i> Summary</a></li>
        <li ><a href="/repo/pqc/mce/changelog"><i class="icon-time"></i> Changelog</a></li>
        <li class="current"><a href="/repo/pqc/mce/files/tip/"><i class="icon-file"></i> Files</a></li>
        <li >
          <a href="#" id="branch_tag_switcher_2" class="dropdown"><i class="icon-random"></i> Switch To</a>
          <ul id="switch_to_list_2" class="switch_to submenu">
            <li><a href="#">Loading...</a></li>
          </ul>
        </li>
        <li >
               <a href="#" class="dropdown"><i class="icon-cogs"></i> Options</a>
          <ul>
              <li><a href="/repo/pqc/mce/compare"><i class="icon-loop"></i> Compare</a></li>

              <li><a href="/repo/pqc/mce/search"><i class="icon-search"></i> Search</a></li>

             </ul>
        </li>
        <li >
          <a href="/repo/pqc/mce/pull-request" title="Show Pull Requests for pqc/mce"> <i class="icon-code-fork"></i> Pull Requests
          </a>
        </li>
      </ul>
  </div>
  <script type="text/javascript">
      YUE.on('branch_tag_switcher_2','mouseover',function(){
         var loaded = YUD.hasClass('branch_tag_switcher_2','loaded');
         if(!loaded){
             YUD.addClass('branch_tag_switcher_2','loaded');
             ypjax("/repo/pqc/mce/branches-tags",'switch_to_list_2',
                 function(o){},
                 function(o){YUD.removeClass('branch_tag_switcher_2','loaded');}
                 ,null);
         }
         return false;
      });
  </script>
  <!--- END CONTEXT BAR -->

<div class="box">
    <!-- box / title -->
    <div class="title">
        
    <div class="breadcrumbs">
    
    Files
        @ r22:97e295009962

    </div>

        <ul class="links">
            <li>
              <span style="text-transform: uppercase;"><a href="#">Branch: </a></span>
            </li>
        </ul>
    </div>
    <div class="table">
        <div id="files_data">
                <h3 class="files_location">
        Location: <a class="ypjax-link" href="/repo/pqc/mce/files/97e2950099623bba7e79dab038df386cd774d48b/">pqc/mce</a>/<a class="ypjax-link" href="/repo/pqc/mce/files/97e2950099623bba7e79dab038df386cd774d48b/vmaconly.py">vmaconly.py</a>
    </h3>
            <div id="node_history" style="padding: 0px 0px 10px 0px">
    <div>
        <div style="float:left">
        <form action="/repo/pqc/mce/diff/vmaconly.py" method="get">
        <input id="diff2" name="diff2" type="hidden" value="e186ffb20977acfdfcf7cbf07b0275974de3bc84" />
        <input id="diff1" name="diff1" type="hidden" />
        <input class="btn btn-small" id="diff" name="diff" type="submit" value="Diff to Revision" />
        <input class="btn btn-small" id="show_rev" name="show_rev" type="submit" value="Show at Revision" />
        <input id="annotate" name="annotate" type="hidden" value="False" />
        <a class="btn btn-small" href="/repo/pqc/mce/changelog/e186ffb20977acfdfcf7cbf07b0275974de3bc84/vmaconly.py">Show Full History</a>
        <a class="btn btn-small" href="#" id="show_authors">Show Authors</a>

        </form>
        </div>
        <div id="file_authors" class="file_author" style="clear:both; display: none"></div>
    </div>
    <div style="clear:both"></div>
</div>


<div id="body" class="codeblock">
    <div class="code-header">
        <div class="stats">
            <div class="left img"><i class="icon-file"></i></div>
            <div class="left item"><pre class="tooltip" title="Thu, 06 Aug 2020 14:21:33"><a href="/repo/pqc/mce/changeset/e186ffb20977acfdfcf7cbf07b0275974de3bc84">r9:e186ffb20977</a></pre></div>
            <div class="left item"><pre>2.2 KiB</pre></div>
            <div class="left item last"><pre>text/x-python</pre></div>
            <div class="buttons">
                <a class="btn btn-mini" href="/repo/pqc/mce/annotate/e186ffb20977acfdfcf7cbf07b0275974de3bc84/vmaconly.py">Show Annotation</a>
              <a class="btn btn-mini" href="/repo/pqc/mce/raw/e186ffb20977acfdfcf7cbf07b0275974de3bc84/vmaconly.py">Show as Raw</a>
              <a class="btn btn-mini" href="/repo/pqc/mce/rawfile/e186ffb20977acfdfcf7cbf07b0275974de3bc84/vmaconly.py">Download as Raw</a>
            </div>
        </div>
        <div class="author">
            <div class="gravatar">
                <img alt="gravatar" src="/repo/images/user16.png"/>
            </div>
            <div title="Joo Cho &lt;jooc@adva.com&gt;" class="user">Joo Cho</div>
        </div>
        <div class="commit">Updated vinit.sh and vresp.sh. Changed adva@ to root@
</div>
    </div>
    <div class="code-body">
              <table class="code-highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><a href="#L1">  1</a>
<a href="#L2">  2</a>
<a href="#L3">  3</a>
<a href="#L4">  4</a>
<a href="#L5">  5</a>
<a href="#L6">  6</a>
<a href="#L7">  7</a>
<a href="#L8">  8</a>
<a href="#L9">  9</a>
<a href="#L10"> 10</a>
<a href="#L11"> 11</a>
<a href="#L12"> 12</a>
<a href="#L13"> 13</a>
<a href="#L14"> 14</a>
<a href="#L15"> 15</a>
<a href="#L16"> 16</a>
<a href="#L17"> 17</a>
<a href="#L18"> 18</a>
<a href="#L19"> 19</a>
<a href="#L20"> 20</a>
<a href="#L21"> 21</a>
<a href="#L22"> 22</a>
<a href="#L23"> 23</a>
<a href="#L24"> 24</a>
<a href="#L25"> 25</a>
<a href="#L26"> 26</a>
<a href="#L27"> 27</a>
<a href="#L28"> 28</a>
<a href="#L29"> 29</a>
<a href="#L30"> 30</a>
<a href="#L31"> 31</a>
<a href="#L32"> 32</a>
<a href="#L33"> 33</a>
<a href="#L34"> 34</a>
<a href="#L35"> 35</a>
<a href="#L36"> 36</a>
<a href="#L37"> 37</a>
<a href="#L38"> 38</a>
<a href="#L39"> 39</a>
<a href="#L40"> 40</a>
<a href="#L41"> 41</a>
<a href="#L42"> 42</a>
<a href="#L43"> 43</a>
<a href="#L44"> 44</a>
<a href="#L45"> 45</a>
<a href="#L46"> 46</a>
<a href="#L47"> 47</a>
<a href="#L48"> 48</a>
<a href="#L49"> 49</a>
<a href="#L50"> 50</a>
<a href="#L51"> 51</a>
<a href="#L52"> 52</a>
<a href="#L53"> 53</a>
<a href="#L54"> 54</a>
<a href="#L55"> 55</a>
<a href="#L56"> 56</a>
<a href="#L57"> 57</a>
<a href="#L58"> 58</a>
<a href="#L59"> 59</a>
<a href="#L60"> 60</a>
<a href="#L61"> 61</a>
<a href="#L62"> 62</a>
<a href="#L63"> 63</a>
<a href="#L64"> 64</a>
<a href="#L65"> 65</a>
<a href="#L66"> 66</a>
<a href="#L67"> 67</a>
<a href="#L68"> 68</a>
<a href="#L69"> 69</a>
<a href="#L70"> 70</a>
<a href="#L71"> 71</a>
<a href="#L72"> 72</a>
<a href="#L73"> 73</a>
<a href="#L74"> 74</a>
<a href="#L75"> 75</a>
<a href="#L76"> 76</a>
<a href="#L77"> 77</a>
<a href="#L78"> 78</a>
<a href="#L79"> 79</a>
<a href="#L80"> 80</a>
<a href="#L81"> 81</a>
<a href="#L82"> 82</a>
<a href="#L83"> 83</a>
<a href="#L84"> 84</a>
<a href="#L85"> 85</a>
<a href="#L86"> 86</a>
<a href="#L87"> 87</a>
<a href="#L88"> 88</a>
<a href="#L89"> 89</a>
<a href="#L90"> 90</a>
<a href="#L91"> 91</a>
<a href="#L92"> 92</a>
<a href="#L93"> 93</a>
<a href="#L94"> 94</a>
<a href="#L95"> 95</a>
<a href="#L96"> 96</a>
<a href="#L97"> 97</a>
<a href="#L98"> 98</a>
<a href="#L99"> 99</a>
<a href="#L100">100</a>
<a href="#L101">101</a>
<a href="#L102">102</a>
<a href="#L103">103</a>
<a href="#L104">104</a>
<a href="#L105">105</a></pre></div></td><td id="hlcode" class="code"><div class="code-highlight"><pre><div id="L1"><a name="L-1"></a><span class="c">#! /usr/bin/env python</span>
</div><div id="L2"><a name="L-2"></a><span class="c"># coding=utf-8</span>
</div><div id="L3"><a name="L-3"></a><span class="c">##############################################</span>
</div><div id="L4"><a name="L-4"></a><span class="c"># Copyright (c) 2020</span>
</div><div id="L5"><a name="L-5"></a><span class="c"># ADVA Optical Networking</span>
</div><div id="L6"><a name="L-6"></a><span class="c">##############################################</span>
</div><div id="L7"><a name="L-7"></a><span class="n">__version__</span> <span class="o">=</span> <span class="s">&quot;0.0&quot;</span>
</div><div id="L8"><a name="L-8"></a>
</div><div id="L9"><a name="L-9"></a><span class="kn">import</span> <span class="nn">os</span>
</div><div id="L10"><a name="L-10"></a><span class="kn">import</span> <span class="nn">binascii</span>
</div><div id="L11"><a name="L-11"></a><span class="kn">import</span> <span class="nn">commands</span>
</div><div id="L12"><a name="L-12"></a><span class="kn">import</span> <span class="nn">time</span>
</div><div id="L13"><a name="L-13"></a><span class="kn">import</span> <span class="nn">base64</span>
</div><div id="L14"><a name="L-14"></a><span class="kn">import</span> <span class="nn">codecs</span>
</div><div id="L15"><a name="L-15"></a><span class="kn">import</span> <span class="nn">hashlib</span> 
</div><div id="L16"><a name="L-16"></a><span class="kn">import</span> <span class="nn">hmac</span> 
</div><div id="L17"><a name="L-17"></a><span class="kn">import</span> <span class="nn">sys</span>
</div><div id="L18"><a name="L-18"></a><span class="kn">import</span> <span class="nn">constants</span>
</div><div id="L19"><a name="L-19"></a>
</div><div id="L20"><a name="L-20"></a><span class="kn">from</span> <span class="nn">ctypes</span> <span class="kn">import</span> <span class="o">*</span>
</div><div id="L21"><a name="L-21"></a>
</div><div id="L22"><a name="L-22"></a><span class="n">host</span> <span class="o">=</span> <span class="s">&quot;root@20.20.20.52&quot;</span>
</div><div id="L23"><a name="L-23"></a>
</div><div id="L24"><a name="L-24"></a><span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">:]):</span>
</div><div id="L25"><a name="L-25"></a>	<span class="n">host</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
</div><div id="L26"><a name="L-26"></a>
</div><div id="L27"><a name="L-27"></a><span class="n">path_near</span> <span class="o">=</span> <span class="n">constants</span><span class="o">.</span><span class="n">BASE_PATH</span><span class="o">+</span><span class="s">&quot;alice/&quot;</span>
</div><div id="L28"><a name="L-28"></a><span class="n">path_far</span> <span class="o">=</span> <span class="n">constants</span><span class="o">.</span><span class="n">BASE_PATH</span><span class="o">+</span><span class="s">&quot;bob/&quot;</span>
</div><div id="L29"><a name="L-29"></a><span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">2</span><span class="p">:]):</span>
</div><div id="L30"><a name="L-30"></a>	<span class="n">path_near</span> <span class="o">=</span> <span class="n">constants</span><span class="o">.</span><span class="n">BASE_PATH</span><span class="o">+</span><span class="s">&quot;bob/&quot;</span>
</div><div id="L31"><a name="L-31"></a>	<span class="n">path_far</span> <span class="o">=</span> <span class="n">constants</span><span class="o">.</span><span class="n">BASE_PATH</span><span class="o">+</span><span class="s">&quot;alice/&quot;</span>
</div><div id="L32"><a name="L-32"></a>
</div><div id="L33"><a name="L-33"></a><span class="n">hybridkey</span> <span class="o">=</span> <span class="s">&quot;&quot;</span>
</div><div id="L34"><a name="L-34"></a><span class="c">########################</span>
</div><div id="L35"><a name="L-35"></a><span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isfile</span><span class="p">(</span><span class="s">&#39;./qkdkey.txt&#39;</span><span class="p">):</span>
</div><div id="L36"><a name="L-36"></a>    <span class="n">dh_sharedkey</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="s">&quot;qkdkey.txt&quot;</span><span class="p">,</span> <span class="s">&quot;r&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
</div><div id="L37"><a name="L-37"></a>    <span class="n">hybridkey</span> <span class="o">+=</span> <span class="n">dh_sharedkey</span>
</div><div id="L38"><a name="L-38"></a>    <span class="k">print</span><span class="p">(</span><span class="s">&quot;QKD key is added.&quot;</span><span class="p">)</span>
</div><div id="L39"><a name="L-39"></a>
</div><div id="L40"><a name="L-40"></a><span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isfile</span><span class="p">(</span><span class="s">&#39;./dhkey.txt&#39;</span><span class="p">):</span>
</div><div id="L41"><a name="L-41"></a>    <span class="n">dh_sharedkey</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="s">&quot;dhkey.txt&quot;</span><span class="p">,</span> <span class="s">&quot;r&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
</div><div id="L42"><a name="L-42"></a>    <span class="n">hybridkey</span> <span class="o">+=</span> <span class="n">dh_sharedkey</span>
</div><div id="L43"><a name="L-43"></a>    <span class="k">print</span><span class="p">(</span><span class="s">&quot;DH key is added.&quot;</span><span class="p">)</span>
</div><div id="L44"><a name="L-44"></a>
</div><div id="L45"><a name="L-45"></a><span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isfile</span><span class="p">(</span><span class="s">&#39;./sharedKey.txt&#39;</span><span class="p">):</span>
</div><div id="L46"><a name="L-46"></a>    <span class="n">mce_sharedkey</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="s">&quot;sharedKey.txt&quot;</span><span class="p">,</span> <span class="s">&quot;r&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
</div><div id="L47"><a name="L-47"></a>    <span class="n">hybridkey</span> <span class="o">+=</span> <span class="n">mce_sharedkey</span>
</div><div id="L48"><a name="L-48"></a>    <span class="k">print</span><span class="p">(</span><span class="s">&quot;MCE key is added.&quot;</span><span class="p">)</span>
</div><div id="L49"><a name="L-49"></a>
</div><div id="L50"><a name="L-50"></a><span class="n">h</span> <span class="o">=</span> <span class="n">hmac</span><span class="o">.</span><span class="n">new</span><span class="p">(</span><span class="s">&quot;SAFE&quot;</span><span class="p">,</span> <span class="n">hybridkey</span><span class="p">,</span> <span class="n">hashlib</span><span class="o">.</span><span class="n">sha256</span><span class="p">)</span>
</div><div id="L51"><a name="L-51"></a><span class="c">#hmac.update(mce_sharedkey)</span>
</div><div id="L52"><a name="L-52"></a><span class="n">mac</span> <span class="o">=</span> <span class="n">h</span><span class="o">.</span><span class="n">hexdigest</span><span class="p">()</span>
</div><div id="L53"><a name="L-53"></a><span class="k">print</span><span class="p">(</span><span class="s">&quot;MAC = &quot;</span><span class="p">)</span>
</div><div id="L54"><a name="L-54"></a><span class="k">print</span><span class="p">(</span><span class="n">mac</span><span class="p">)</span>
</div><div id="L55"><a name="L-55"></a>
</div><div id="L56"><a name="L-56"></a><span class="c"># mac transmission </span>
</div><div id="L57"><a name="L-57"></a><span class="n">f</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="s">&quot;mac.txt&quot;</span><span class="p">,</span> <span class="s">&quot;w+&quot;</span><span class="p">)</span>
</div><div id="L58"><a name="L-58"></a><span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">mac</span><span class="p">)</span>
</div><div id="L59"><a name="L-59"></a><span class="n">f</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
</div><div id="L60"><a name="L-60"></a>
</div><div id="L61"><a name="L-61"></a><span class="c"># store mac in the local folder</span>
</div><div id="L62"><a name="L-62"></a><span class="n">cmd</span> <span class="o">=</span> <span class="s">&quot;cp mac.txt &quot;</span> <span class="o">+</span> <span class="n">path_near</span>
</div><div id="L63"><a name="L-63"></a><span class="k">print</span><span class="p">(</span><span class="n">cmd</span><span class="p">)</span>
</div><div id="L64"><a name="L-64"></a><span class="p">(</span><span class="n">err</span><span class="p">,</span><span class="n">output</span><span class="p">)</span> <span class="o">=</span> <span class="n">commands</span><span class="o">.</span><span class="n">getstatusoutput</span><span class="p">(</span><span class="n">cmd</span><span class="p">)</span>
</div><div id="L65"><a name="L-65"></a><span class="k">print</span><span class="p">(</span><span class="n">err</span><span class="p">)</span>
</div><div id="L66"><a name="L-66"></a><span class="k">print</span><span class="p">(</span><span class="n">output</span><span class="p">)</span>
</div><div id="L67"><a name="L-67"></a>
</div><div id="L68"><a name="L-68"></a><span class="n">cmd</span> <span class="o">=</span> <span class="s">&quot;scp mac.txt &quot;</span> <span class="o">+</span> <span class="n">host</span> <span class="o">+</span> <span class="s">&quot;:&quot;</span> <span class="o">+</span> <span class="n">path_near</span>
</div><div id="L69"><a name="L-69"></a><span class="k">print</span><span class="p">(</span><span class="n">cmd</span><span class="p">)</span>
</div><div id="L70"><a name="L-70"></a><span class="p">(</span><span class="n">err</span><span class="p">,</span><span class="n">output</span><span class="p">)</span> <span class="o">=</span> <span class="n">commands</span><span class="o">.</span><span class="n">getstatusoutput</span><span class="p">(</span><span class="n">cmd</span><span class="p">)</span>
</div><div id="L71"><a name="L-71"></a><span class="k">print</span><span class="p">(</span><span class="n">err</span><span class="p">)</span>
</div><div id="L72"><a name="L-72"></a><span class="k">print</span><span class="p">(</span><span class="n">output</span><span class="p">)</span>
</div><div id="L73"><a name="L-73"></a>
</div><div id="L74"><a name="L-74"></a><span class="n">cmd</span> <span class="o">=</span> <span class="s">&quot;ssh &quot;</span> <span class="o">+</span> <span class="n">host</span>  <span class="o">+</span> <span class="s">&quot; stat &quot;</span> <span class="o">+</span> <span class="n">path_far</span> <span class="o">+</span> <span class="s">&quot;mac.txt&quot;</span> 
</div><div id="L75"><a name="L-75"></a><span class="k">print</span><span class="p">(</span><span class="n">cmd</span><span class="p">)</span>
</div><div id="L76"><a name="L-76"></a><span class="n">err</span> <span class="o">=</span> <span class="mi">1</span>
</div><div id="L77"><a name="L-77"></a><span class="k">print</span><span class="p">(</span><span class="s">&quot;Waiting for the MAC from the remote side...&quot;</span><span class="p">)</span>
</div><div id="L78"><a name="L-78"></a><span class="k">while</span> <span class="n">err</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">:</span>
</div><div id="L79"><a name="L-79"></a>	<span class="p">(</span><span class="n">err</span><span class="p">,</span><span class="n">output</span><span class="p">)</span> <span class="o">=</span> <span class="n">commands</span><span class="o">.</span><span class="n">getstatusoutput</span><span class="p">(</span><span class="n">cmd</span><span class="p">)</span>
</div><div id="L80"><a name="L-80"></a><span class="c">#	print(err)</span>
</div><div id="L81"><a name="L-81"></a>
</div><div id="L82"><a name="L-82"></a>	<span class="k">if</span> <span class="n">err</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span> 
</div><div id="L83"><a name="L-83"></a>		<span class="n">cmd</span> <span class="o">=</span> <span class="s">&quot;scp &quot;</span> <span class="o">+</span> <span class="n">host</span> <span class="o">+</span> <span class="s">&quot;:&quot;</span> <span class="o">+</span> <span class="n">path_far</span> <span class="o">+</span> <span class="s">&quot;mac.txt &quot;</span> <span class="o">+</span> <span class="s">&quot;./mac_far.txt&quot;</span>
</div><div id="L84"><a name="L-84"></a>		<span class="p">(</span><span class="n">err</span><span class="p">,</span><span class="n">output</span><span class="p">)</span> <span class="o">=</span> <span class="n">commands</span><span class="o">.</span><span class="n">getstatusoutput</span><span class="p">(</span><span class="n">cmd</span><span class="p">)</span>
</div><div id="L85"><a name="L-85"></a>		<span class="k">print</span><span class="p">(</span><span class="n">err</span><span class="p">)</span>
</div><div id="L86"><a name="L-86"></a>	<span class="k">else</span><span class="p">:</span>
</div><div id="L87"><a name="L-87"></a>		<span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</div><div id="L88"><a name="L-88"></a><span class="c">#		print(&quot;bob/ct.txt does not exist.&quot;)</span>
</div><div id="L89"><a name="L-89"></a>
</div><div id="L90"><a name="L-90"></a>
</div><div id="L91"><a name="L-91"></a><span class="c"># remove  mac_far.txt </span>
</div><div id="L92"><a name="L-92"></a><span class="n">cmd</span> <span class="o">=</span> <span class="s">&quot;ssh &quot;</span> <span class="o">+</span> <span class="n">host</span>  <span class="o">+</span> <span class="s">&quot; rm &quot;</span> <span class="o">+</span> <span class="n">path_far</span> <span class="o">+</span> <span class="s">&quot;mac.txt&quot;</span> 
</div><div id="L93"><a name="L-93"></a><span class="k">print</span><span class="p">(</span><span class="n">cmd</span><span class="p">)</span>
</div><div id="L94"><a name="L-94"></a><span class="p">(</span><span class="n">err</span><span class="p">,</span><span class="n">output</span><span class="p">)</span> <span class="o">=</span> <span class="n">commands</span><span class="o">.</span><span class="n">getstatusoutput</span><span class="p">(</span><span class="n">cmd</span><span class="p">)</span>
</div><div id="L95"><a name="L-95"></a><span class="k">print</span><span class="p">(</span><span class="n">err</span><span class="p">)</span>
</div><div id="L96"><a name="L-96"></a>
</div><div id="L97"><a name="L-97"></a><span class="n">mac_far</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="s">&quot;mac_far.txt&quot;</span><span class="p">,</span> <span class="s">&quot;r&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
</div><div id="L98"><a name="L-98"></a><span class="k">if</span> <span class="n">mac</span> <span class="o">==</span> <span class="n">mac_far</span><span class="p">:</span>
</div><div id="L99"><a name="L-99"></a>	<span class="k">print</span><span class="p">(</span><span class="s">&quot;the final key is verified!&quot;</span><span class="p">)</span>
</div><div id="L100"><a name="L-100"></a><span class="k">else</span><span class="p">:</span>
</div><div id="L101"><a name="L-101"></a>	<span class="k">print</span><span class="p">(</span><span class="s">&quot;ERROR: the final key is NOT verified!&quot;</span><span class="p">)</span>
</div><div id="L102"><a name="L-102"></a>
</div><div id="L103"><a name="L-103"></a><span class="k">print</span><span class="p">(</span><span class="s">&quot;Done&quot;</span><span class="p">)</span>
</div><div id="L104"><a name="L-104"></a>
</div><div id="L105"><a name="L-105"></a>
</div></pre></div>
</td></tr></table>
    </div>
</div>

<script>
    $(document).ready(function(){
        // fake html5 history state
        var _State = {
           url: "/repo/pqc/mce/files/97e2950099623bba7e79dab038df386cd774d48b/vmaconly.py",
           data: {
             node_list_url: node_list_url.replace('__REV__',"97e2950099623bba7e79dab038df386cd774d48b").replace('__FPATH__', "vmaconly.py"),
             url_base: url_base.replace('__REV__',"97e2950099623bba7e79dab038df386cd774d48b"),
             rev:"97e2950099623bba7e79dab038df386cd774d48b",
             f_path: "vmaconly.py"
           }
        }
        callbacks(_State) // defined in files.html, main callbacks. Triggerd in pjax calls
    })
</script>


        </div>
    </div>
</div>

<script type="text/javascript">
var CACHE = {};
var CACHE_EXPIRE = 5*60*1000; //cache for 5*60s
//used to construct links from the search list
var url_base = '/repo/pqc/mce/files/__REV__/__FPATH__';
//send the nodelist request to this url
var node_list_url = '/repo/pqc/mce/nodelist/__REV__/__FPATH__';
// send the node history requst to this url
var node_history_url = '/repo/pqc/mce/history/__REV__/__FPATH__';

pyroutes.register('files_nodelist_home', "/repo/pqc/mce/nodelist/%25%28revision%29s/%25%28f_path%29s", ['revision', 'f_path']);
pyroutes.register('files_history_home', "/repo/pqc/mce/history/%25%28revision%29s/%25%28f_path%29s", ['revision', 'f_path']);
pyroutes.register('files_authors_home', "/repo/pqc/mce/authors/%25%28revision%29s/%25%28f_path%29s", ['revision', 'f_path']);

var ypjax_links = function(){
    YUE.on(YUQ('.ypjax-link'), 'click',function(e){

        //don't do ypjax on middle click
        if(e.which == 2 || !History.enabled){
            return true;
        }

        var el = e.currentTarget;
        var url = el.href;

        var _base_url = '/repo/pqc/mce/files//';
        _base_url = _base_url.replace('//','/')

        //extract rev and the f_path from url.
        parts = url.split(_base_url)
        if(parts.length != 2){
            return false;
        }

        var parts2 = parts[1].split('/');
        var rev = parts2.shift(); // pop the first element which is the revision
        var f_path = parts2.join('/');

        //page title make this consistent with title() mako function on top
        var title = "pqc/mce Files" + " &middot; " + (f_path || '\\') + " &middot; " + "APT Repository";

        var _node_list_url = node_list_url.replace('__REV__',rev).replace('__FPATH__', f_path);
        var _url_base = url_base.replace('__REV__',rev);

        // Change our States and save some data for handling events
        var data = {url:url,title:title, url_base:_url_base,
                    node_list_url:_node_list_url, rev:rev, f_path:f_path};
        History.pushState(data, title, url);

        //now we're sure that we can do ypjax things
        YUE.preventDefault(e);
        return false;
    });
}

// callbacks needed to process the pjax filebrowser
var callbacks = function(State){
    ypjax_links();
    tooltip_activate();

    if(State !== undefined){
        //inistially loaded stuff
        var _f_path = State.data.f_path;
        var _rev = State.data.rev;

        fileBrowserListeners(State.url, State.data.node_list_url, State.data.url_base);
        // Inform Google Analytics of the change
        if ( typeof window.pageTracker !== 'undefined' ) {
            window.pageTracker._trackPageview(State.url);
        }
    }

    function highlight_lines(lines){
        for(pos in lines){
          YUD.setStyle('L'+lines[pos],'background-color','#FFFFBE');
        }
    }
    page_highlights = location.href.substring(location.href.indexOf('#')+1).split('L');
    if (page_highlights.length == 2){
       highlight_ranges  = page_highlights[1].split(",");

       var h_lines = [];
       for (pos in highlight_ranges){
            var _range = highlight_ranges[pos].split('-');
            if(_range.length == 2){
                var start = parseInt(_range[0]);
                var end = parseInt(_range[1]);
                if (start < end){
                    for(var i=start;i<=end;i++){
                        h_lines.push(i);
                    }
                }
            }
            else{
                h_lines.push(parseInt(highlight_ranges[pos]));
            }
      }
      highlight_lines(h_lines);
      var _first_line= YUD.get('L'+h_lines[0]);
      if(_first_line){
          _first_line.scrollIntoView()
      }
    }

    // select code link event
    YUE.on('hlcode', 'mouseup', getSelectionLink);

    // history select field
    var cache = {}
    $("#diff1").select2({
        placeholder: _TM['Select changeset'],
        dropdownAutoWidth: true,
        query: function(query){
          var key = 'cache';
          var cached = cache[key] ;
          if(cached) {
            var data = {results: []};
            //filter results
            $.each(cached.results, function(){
                var section = this.text;
                var children = [];
                $.each(this.children, function(){
                    if(query.term.length == 0 || this.text.toUpperCase().indexOf(query.term.toUpperCase()) >= 0 ){
                        children.push({'id': this.id, 'text': this.text})
                    }
                })
                data.results.push({'text': section, 'children': children})
            });
            query.callback(data);
          }else{
              $.ajax({
                url: pyroutes.url('files_history_home', {'revision': _rev, 'f_path': _f_path}),
                data: {},
                dataType: 'json',
                type: 'GET',
                success: function(data) {
                  cache[key] = data;
                  query.callback({results: data.results});
                }
              })
          }
        },
    });
    $('#show_authors').on('click', function(){
        $.ajax({
            url: pyroutes.url('files_authors_home', {'revision': _rev, 'f_path': _f_path}),
            success: function(data) {
                $('#file_authors').html(data);
                $('#file_authors').show();
                tooltip_activate()
            }
        })
    })
}

YUE.onDOMReady(function(){
    ypjax_links();
    var container = 'files_data';
    //Bind to StateChange Event
    History.Adapter.bind(window,'statechange',function(){
        var State = History.getState();
        cache_key = State.url;
        //check if we have this request in cache maybe ?
        var _cache_obj = CACHE[cache_key];
        var _cur_time = new Date().getTime();
        // get from cache if it's there and not yet expired !
        if(_cache_obj !== undefined && _cache_obj[0] > _cur_time){
            YUD.get(container).innerHTML=_cache_obj[1];
            YUD.setStyle(container,'opacity','1.0');

            //callbacks after ypjax call
            callbacks(State);
        }
        else{
          ypjax(State.url,container,function(o){
              //callbacks after ypjax call
              callbacks(State);
              if (o !== undefined){
                //store our request in cache
                var _expire_on = new Date().getTime()+CACHE_EXPIRE;
              CACHE[cache_key] = [_expire_on, o.responseText];
            }
          });
        }
    });

    // init the search filter
    var _State = {
       url: "/repo/pqc/mce/files/97e2950099623bba7e79dab038df386cd774d48b/vmaconly.py",
       data: {
         node_list_url: node_list_url.replace('__REV__',"97e2950099623bba7e79dab038df386cd774d48b").replace('__FPATH__', "vmaconly.py"),
         url_base: url_base.replace('__REV__',"97e2950099623bba7e79dab038df386cd774d48b"),
         rev:"97e2950099623bba7e79dab038df386cd774d48b",
         f_path: "vmaconly.py"
       }
    }
    fileBrowserListeners(_State.url, _State.data.node_list_url, _State.data.url_base);
});

</script>


    </div>
</div>
<!-- END CONTENT -->

<!-- FOOTER -->
<div id="footer">
   <div id="footer-inner" class="title">
       <div>
           <p class="footer-link">
               
           </p>
           <p class="footer-link-right">
               RhodeCode
                   2.1.0
               &copy; 2010-2020, <a href="https://rhodecode.com">RhodeCode GmbH</a>. All rights reserved.
                   &ndash; <a href="https://rhodecode.com/help/">Support</a>
           </p>
       </div>
   </div>
</div>

<!-- END FOOTER -->

















<div class="modal" id="help_kb" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
          <h4 class="modal-title">Keyboard shortcuts</h4>
        </div>
        <div class="modal-body">
           <div class="row">
              <div class="col-md-5">
                <table class="keyboard-mappings">
                    <tbody>
                  <tr>
                    <th></th>
                    <th>Site-wide shortcuts</th>
                  </tr>
                  
                  <tr>
                    <td class="keys">
                      <span class="key">/</span>
                    </td>
                    <td>Open quick search box</td>
                  </tr>
                  <tr>
                    <td class="keys">
                      <span class="key">ctrl/cmd+b</span>
                    </td>
                    <td>Show main settings bar</td>
                  </tr>
                  <tr>
                    <td class="keys">
                      <span class="key">g h</span>
                    </td>
                    <td>Goto home page</td>
                  </tr>
                  <tr>
                    <td class="keys">
                      <span class="key">n r</span>
                    </td>
                    <td>New repository page</td>
                  </tr>
                  <tr>
                    <td class="keys">
                      <span class="key">n g</span>
                    </td>
                    <td>New gist page</td>
                  </tr>
                </tbody>
                  </table>
              </div>
              <div class="col-md-offset-5">
                <table class="keyboard-mappings">
                <tbody>
                  <tr>
                    <th></th>
                    <th>Repositories</th>
                  </tr>
                  
                  <tr>
                    <td class="keys">
                      <span class="key">g s</span>
                    </td>
                    <td>Goto summary page</td>
                  </tr>
                  <tr>
                    <td class="keys">
                      <span class="key">g c</span>
                    </td>
                    <td>Goto changelog page</td>
                  </tr>
                  <tr>
                    <td class="keys">
                      <span class="key">g f</span>
                    </td>
                    <td>Goto files page</td>
                  </tr>
                  <tr>
                    <td class="keys">
                      <span class="key">g o</span>
                    </td>
                    <td>Goto repository options</td>
                  </tr>
                </tbody>
            </table>
              </div>
            </div>
        </div>
        <div class="modal-footer">
        </div>
      </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div><!-- /.modal -->

    </body>
</html>
