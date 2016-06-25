MAILGUN_KEY = ENV['MAILGUN_KEY']
MAILGUN_DOMAIN = ENV['MAILGUN_DOMAIN']

module SendEmail
  @queue = :mailer

  def self.perform(oe_id)
    oe = OutgoingEmail.find_by_id oe_id
    puts "Processing email to #{oe.to}"
    client = Mailgun::Client.new MAILGUN_KEY
    message_params = oe.as_json.slice('from', 'to', 'subject', 'text')
    puts message_params
    unless MAILGUN_KEY && MAILGUN_DOMAIN
      puts '(No mailgun config; skipping actual send)'
      return 'ok'
    end

    result = client.send_message MAILGUN_DOMAIN, message_params
    puts result.body
  end
end
