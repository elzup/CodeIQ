class Container
  class << self
    def <<(converter)
      @converters ||= []
      @converters << converter
    end
    def converters
      @converters
    end
  end
end
module Converters
  class Base
    class << self
      def extended(child)
        Container << child
      end
      def condition(number)
        fail NotImplementedError, 'you must implement condition method'
      end
      def convert(number)
        fail NotImplementedError, 'you must implement convert method'
      end
    end
  end
end
module FizzBuzz
  module Converters
    class FizzBuzzConverter < ::Converters::Base
      class << self
        def condition(number)
          number % 15 == 0
        end
        def convert(number)
          'FizzBuzz'
        end
      end
    end
    class FizzConverter < ::Converters::Base
      class << self
        def condition(number)
          number % 3 == 0
        end
        def convert(number)
          'Fizz'
        end
      end
    end
    class BuzzConverter < ::Converters::Base
      class << self
        def condition(number)
          number % 5 == 0
        end
        def convert(number)
          'Buzz'
        end
      end
    end
  end
  class Executor
    def self.execute(from, to)
      (from..to).each_with_object([]) do |i, memo|
        converter = Container.converters.find { |e|e.condition(i) }
        memo << (converter ? converter.convert(i) : i)
      end.join(',')
    end
  end
end
module FizzBuzz
  module Converters
    class CodeIQConverter < ::Converters::Base
      class << self
        def condition(number)
          number % 7 == 0
        end
        def convert(number)
          'CodeIQ'
        end
      end
    end
  end
end
print FizzBuzz::Executor.execute(1, 30), "\n"
