module SendEmail
  @queue = :mailer

  def self.perform(oe_id)
    oe = OutgoingEmail.find_by_id oe_id
    puts "Processing email to #{oe.to}"
  end
end
