class OutgoingEmailsController < ApplicationController
  def index
    @outgoing_emails = OutgoingEmail.all
    render json: @outgoing_emails
  end

  def show
    @oe = OutgoingEmail.find params[:id]
    render json: @oe
  end

  def create
    oe = OutgoingEmail.new email_params
    if oe.save
      Resque.enqueue(SendEmail, oe.id)
      render json: oe, status: 201, location: oe
    else
      render json: { errors: oe.errors }, status: 422
    end
  end

  private

  def email_params
    params.permit :to, :from, :subject, :text
  end
end
