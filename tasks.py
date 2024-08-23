from crewai import Task
from textwrap import dedent

"""
Creating Tasks Cheat Sheet:
- Begin with the end in mind. Identify the specific outcome your tasks are aiming to achieve.
- Break down the outcome into actionable tasks, assigning each task to the appropriate agent.
- Ensure tasks are descriptive, providing clear instructions and expected deliverables.

Goal:
- Develop a detailed itinerary, including city selection, attractions, and practical travel advice.

Key Steps for Task Creation:
1. Identify the Desired Outcome: Define what success looks like for your project.
    - A detailed 7 day travel itenerary.

2. Task Breakdown: Divide the goal into smaller, manageable tasks that agents can execute.
    - Itenerary Planning: develop a detailed plan for each day of the trip.
    - City Selection: Analayze and pick the best cities to visit.
    - Local Tour Guide: Find a local expert to provide insights and recommendations.

3. Assign Tasks to Agents: Match tasks with agents based on their roles and expertise.

4. Task Description Template:
  - Use this template as a guide to define each task in your CrewAI application. 
  - This template helps ensure that each task is clearly defined, actionable, and aligned with the specific goals of your project.

  Template:
  ---------
  def [task_name](self, agent, [parameters]):
      return Task(description=dedent(f'''
      **Task**: [Provide a concise name or summary of the task.]
      **Description**: [Detailed description of what the agent is expected to do, including actionable steps and expected outcomes. This should be clear and direct, outlining the specific actions required to complete the task.]

      **Parameters**: 
      - [Parameter 1]: [Description]
      - [Parameter 2]: [Description]
      ... [Add more parameters as needed.]

      **Note**: [Optional section for incentives or encouragement for high-quality work. This can include tips, additional context, or motivations to encourage agents to deliver their best work.]

      '''), agent=agent)

"""


class TravelTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def plan_itinerary(self, agent, city, travel_dates,num_of_days, interests):
        return Task(
            description=dedent(
                f"""
            **Task**: Develop a 7-Day Travel Itinerary
            **Description**: Expand the city guide into a full {num_of_days}-day travel itinerary with detailed 
                per-day plans, including weather forecasts, places to eat, packing suggestions, 
                and a budget breakdown. You MUST suggest actual places to visit, actual hotels to stay, 
                and actual restaurants to go to. This itinerary should cover all aspects of the trip, 
                from arrival to departure, integrating the city guide information with practical travel logistics.

            **Parameters**: 
            - City: {city}
            - Trip Date: {travel_dates}
            - Traveler Interests: {interests}

            **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
            max_iterations=10,
            expected_output=dedent(
                f"""
                **Expected Output**: 
                - A complete {num_of_days}-day itinerary with day-by-day plans.
                - Each day should include:
                  - **Date**: Specific dates for each day.
                  - **Activities**: Detailed list of daily activities, including morning, afternoon, and evening plans.
                  - **Budget**: Estimated costs for each day, including transportation, accommodation, food, and activities.
                  - **Accommodation**: Recommendations for hotels or places to stay, including booking details.
                  - **Meals**: Suggested restaurants for breakfast, lunch, and dinner, with average costs per meal.
                  - **Transportation**: Information on how to get from one place to another, including public transport, car rentals, or walking routes.
                  - **Weather**: Daily weather forecast with packing suggestions.
                - The itinerary should ensure that all activities are well-balanced and suited to the traveler’s interests.
                - The final plan should be ready to present to the client, including practical tips and recommendations.
                """
            )
        )

    def identify_city(self, agent, origin, cities, interests, travel_dates, num_of_days):
        return Task(
            description=dedent(
                f"""
                    **Task**:  Identify the Best City for the Trip
                    **Description**: Analyze and select the best city for the trip based on specific 
                        criteria such as weather patterns, seasonal events, and travel costs. 
                        This task involves comparing multiple cities, considering factors like current weather 
                        conditions, upcoming cultural or seasonal events, and overall travel expenses. 
                        Your final answer must be a detailed report on the chosen city, 
                        including actual flight costs, weather forecast, and attractions.


                    **Parameters**: 
                    - Origin: {origin}
                    - Cities: {cities}
                    - Interests: {interests}
                    - Travel Date: {travel_dates}
                    - Number of Days: {num_of_days}

                    **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
            max_iterations=10,
            expected_output=dedent(
                f"""
                **Expected Output**:
                - A comprehensive report on the selected city.
                - The report should include:
                  - **City Name**: The chosen city for the trip.
                  - **Flight Information**: Detailed flight options with costs, flight durations, and airlines.
                  - **Weather Forecast**: {num_of_days}-day weather forecast with daily breakdowns.
                  - **Cultural/Seasonal Events**: Upcoming events during the travel dates.
                  - **Estimated Budget**: A detailed budget for the trip, including flights, accommodation, food, and activities.
                  - **Key Attractions**: A list of must-visit landmarks, museums, parks, and hidden gems with descriptions and estimated costs.
                  - **Transportation Options**: Information on how to travel within the city (public transport, taxis, etc.).
                - This report should provide all the information needed to decide on the best city for the trip.
                """
            )
        )

    def gather_city_info(self, agent, city, travel_dates,num_of_days, interests):
        return Task(
            description=dedent(
                f"""
                    **Task**:  Gather In-depth City Guide Information
                    **Description**: Compile an in-depth guide for the selected city, gathering information about 
                        key attractions, local customs, special events, and daily activity recommendations. 
                        This guide should provide a thorough overview of what the city has to offer, including 
                        hidden gems, cultural hotspots, must-visit landmarks, weather forecasts, and high-level costs.

                    **Parameters**: 
                    - Cities: {city}
                    - Interests: {interests}
                    - Travel Date: {travel_dates}
                    - num_of_days: {num_of_days}

                    **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
            max_iterations=10,
            expected_output=dedent(
                f"""
                **Expected Output**: 
                - A comprehensive city guide including:
                  - **Key Attractions**: A list of at least 10 key attractions with descriptions, opening hours, and entry fees.
                  - **Local Customs**: A summary of the city's local customs and traditions, including etiquette and cultural practices.
                  - **Special Events**: Information on any special events happening during the travel dates.
                  - **Daily Activity Recommendations**: Recommendations for daily activities tailored to the traveler's interests.
                  - **Estimated Costs**: High-level cost estimates for accommodation, food, and attractions per day.
                  - **Weather Forecast**: A detailed weather forecast for the travel dates.
                - The guide should be well-rounded and ready to present to the traveler.
                """
            )
        )