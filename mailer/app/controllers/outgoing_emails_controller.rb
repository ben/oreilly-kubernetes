class OutgoingEmailsController < ApplicationController
  def index
    @outgoing_emails = OutgoingEmail.all
    render json: @outgoing_emails
  end

  def show
    @oe = OutgoingEmail.find params[:id]
    render json: @oe
  end
end
