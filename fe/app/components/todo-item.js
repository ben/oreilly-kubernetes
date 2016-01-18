import Ember from 'ember';

export default Ember.Component.extend({
    actions: {
        complete() {
            this.set('model.state', 'complete');
            this.get('model').save();
        },
        uncomplete() {
            this.set('model.state', null);
            this.get('model').save();
        },
        delete() {
            this.get('model').destroy();
        }
    },

    isComplete: function() {
        return this.get('model.state') == 'complete';
    }.property('model.state')
});
