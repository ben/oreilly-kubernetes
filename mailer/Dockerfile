FROM rails:4.2
EXPOSE 3000
CMD ["rails", "server", "-b", "0.0.0.0"]

RUN mkdir -p /app
WORKDIR /app

COPY Gemfile /app/
COPY Gemfile.lock /app/
RUN bundle config --global frozen 1
RUN bundle install

COPY . /app
