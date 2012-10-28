jQuery(function( $ ) {
    'use strict';

    var Utils = {
    };

    var App = {
        init: function() {
            this.title = 'Flask Boilerplate';
            this.cacheElements();
            this.bindEvents();
            this.render();
        },
        cacheElements: function() {
            this.$title = $('#title');
        },
        bindEvents: function() {
            this.$title.on('hover',this.onHoverTitle);
        },
        onHoverTitle: function(event) {
            event.stopPropagation();
            $(this).toggleClass('bigger');
        },
        render: function() {
            this.$title.text(this.title);
        }
    };

    App.init();

});