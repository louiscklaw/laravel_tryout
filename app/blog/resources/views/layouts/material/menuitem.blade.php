
@foreach($test_menuitems as $test_menuitem)
<li>
    <a href="pages/typography.html">
        <i class="material-icons">content_copy</i>
        <span>{{  $test_menuitem['name']  }}</span>
    </a>
    <!-- find me -->
</li>
@endforeach
