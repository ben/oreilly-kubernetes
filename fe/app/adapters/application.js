import DS from 'ember-data';
import Ember from 'ember';
import ENV from 'fe/config/environment';

export default DS.RESTAdapter.extend({
    host: Ember.computed(function () {
        return ENV.APP.apiHost;
    }),
});
