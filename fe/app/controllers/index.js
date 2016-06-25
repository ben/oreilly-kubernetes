import Ember from 'ember';
import config from '../config/environment';

export default Ember.Controller.extend({
    newTodoTitle: '',
    emailLinkText: 'Send me an email with this list',
    destEmailAddress: '',
    actions: {
        create() {
            var todo = this.store.createRecord('todo', {
                title: this.get('newTodoTitle'),
            });
            todo.save();
            this.set('newTodoTitle', '');
            this.set('emailLinkText', 'Send me an email');
        },

        sendEmail(e) {
          var postUrl = config.APP.apiHost + '/send_email'
          console.log('Sending!', config.APP.apiHost);
          Ember.$.post(postUrl, { to: this.get('destEmailAddress') });
        }
    },
});
