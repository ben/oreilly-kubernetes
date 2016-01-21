import Ember from 'ember';

export default Ember.Controller.extend({
    newTodoTitle: '',
    actions: {
        create() {
            var todo = this.store.createRecord('todo', {
                title: this.get('newTodoTitle'),
            });
            todo.save();
            this.set('newTodoTitle', '');
        },
    },
});
