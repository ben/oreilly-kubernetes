import Ember from 'ember';

export default Ember.Component.extend({
    actions: {
        toggleComplete() {
            var currentState = this.get('model.state');
            this.set('model.state', currentState === 'complete' ? 'open' : 'complete');
            this.get('model').save();
        },
        delete() {
            this.get('model').destroyRecord();
        }
    },

    isComplete: function() {
        console.log(this.get('model.state'));
        return this.get('model.state') === 'complete';
    }.property('model.state')
});
