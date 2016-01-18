import Ember from 'ember';

export default Ember.Controller.extend({
    actions: {
        complete(t) {
            console.log('complete', t);
        },
        delete(t) {
            console.log('delete', t);
        }
    }
});
