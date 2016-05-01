class CreateOutgoingEmailTable < ActiveRecord::Migration
  def change
    create_table :outgoing_emails do |t|
      t.string :to
      t.string :from
      t.string :subject
      t.string :text
      t.timestamps
    end
  end
end
