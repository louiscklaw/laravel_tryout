<a href="javascript:void(0);" class="menu-toggle waves-effect waves-block toggled">
    <span>{{ $slot }}</span>
</a>

    @if (isset($contain_third_menu_items) && $contain_third_menu_items)
        <ul class="ml-menu" style="display: block;">
            @component('layouts.menu.third_menu_item')
                test_3rd_item
            @endcomponent
        </ul>
    @endif
