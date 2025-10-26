"""
Smooth Kafka Animation with Manim
Features:
- Icons fade in gradually
- Arrows grow smoothly
- Text appears with animations
- Professional transitions
"""

from manim import *

class KafkaFlowAnimation(Scene):
    def construct(self):
        # Title
        title = Text("Kafka Event Streaming", font_size=48)
        title.to_edge(UP)
        self.play(Write(title), run_time=1.5)
        self.wait(0.5)
        
        # Producer (left side)
        producer_box = RoundedRectangle(
            width=2.5, 
            height=1.5, 
            corner_radius=0.2,
            fill_color="#FF6B6B",
            fill_opacity=0.8,
            stroke_color="#E53E3E",
            stroke_width=3
        )
        producer_box.shift(LEFT * 4)
        
        producer_text = Text("Checkout\nService", font_size=24, color=WHITE)
        producer_text.move_to(producer_box.get_center())
        producer_label = Text("Producer", font_size=16, color="#FF6B6B")
        producer_label.next_to(producer_box, DOWN, buff=0.2)
        
        # Animate producer appearing
        self.play(
            FadeIn(producer_box, scale=0.8),
            FadeIn(producer_text),
            run_time=1
        )
        self.play(FadeIn(producer_label, shift=UP * 0.3), run_time=0.5)
        self.wait(0.5)
        
        # Kafka Topic (center)
        kafka_box = RoundedRectangle(
            width=3,
            height=2,
            corner_radius=0.2,
            fill_color="#45B7D1",
            fill_opacity=0.8,
            stroke_color="#3182CE",
            stroke_width=3
        )
        
        kafka_text = Text("orders", font_size=32, color=WHITE, weight=BOLD)
        kafka_text.move_to(kafka_box.get_center() + UP * 0.3)
        
        kafka_subtitle = Text("Topic", font_size=20, color=WHITE)
        kafka_subtitle.next_to(kafka_text, DOWN, buff=0.3)
        
        # Partitions
        partition_text = Text("3 Partitions", font_size=16, color=WHITE, slant=ITALIC)
        partition_text.next_to(kafka_subtitle, DOWN, buff=0.2)
        
        # Animate Kafka appearing
        self.play(
            FadeIn(kafka_box, scale=0.8),
            run_time=1
        )
        self.play(
            Write(kafka_text),
            run_time=0.8
        )
        self.play(
            FadeIn(kafka_subtitle),
            FadeIn(partition_text),
            run_time=0.6
        )
        self.wait(0.5)
        
        # Arrow from Producer to Kafka (grows smoothly)
        arrow1 = Arrow(
            producer_box.get_right(),
            kafka_box.get_left(),
            buff=0.1,
            color="#00D9FF",
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15
        )
        
        arrow1_label = Text("Publish Orders", font_size=18, color="#00D9FF")
        arrow1_label.next_to(arrow1, UP, buff=0.2)
        
        # Animate arrow growing
        self.play(
            GrowArrow(arrow1),
            run_time=1.2
        )
        self.play(
            FadeIn(arrow1_label, shift=DOWN * 0.2),
            run_time=0.6
        )
        self.wait(0.5)
        
        # Consumer 1 - Inventory (top right)
        consumer1_box = RoundedRectangle(
            width=2.5,
            height=1.3,
            corner_radius=0.2,
            fill_color="#4ECDC4",
            fill_opacity=0.8,
            stroke_color="#38B2AC",
            stroke_width=3
        )
        consumer1_box.shift(RIGHT * 4 + UP * 1.5)
        
        consumer1_text = Text("Inventory\nManager", font_size=20, color=WHITE)
        consumer1_text.move_to(consumer1_box.get_center())
        
        consumer1_label = Text("Consumer", font_size=14, color="#4ECDC4")
        consumer1_label.next_to(consumer1_box, DOWN, buff=0.2)
        
        # Animate Consumer 1 appearing
        self.play(
            FadeIn(consumer1_box, scale=0.8),
            FadeIn(consumer1_text),
            run_time=1
        )
        self.play(FadeIn(consumer1_label, shift=UP * 0.3), run_time=0.5)
        
        # Arrow from Kafka to Consumer 1
        arrow2 = Arrow(
            kafka_box.get_right() + UP * 0.5,
            consumer1_box.get_left(),
            buff=0.1,
            color="#4ECDC4",
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15
        )
        
        arrow2_label = Text("inventory-group", font_size=16, color="#4ECDC4")
        arrow2_label.next_to(arrow2, UP, buff=0.1)
        
        self.play(
            GrowArrow(arrow2),
            run_time=1.2
        )
        self.play(
            FadeIn(arrow2_label, shift=DOWN * 0.2),
            run_time=0.6
        )
        self.wait(0.5)
        
        # Consumer 2 - Billing (bottom right)
        consumer2_box = RoundedRectangle(
            width=2.5,
            height=1.3,
            corner_radius=0.2,
            fill_color="#96CEB4",
            fill_opacity=0.8,
            stroke_color="#68D391",
            stroke_width=3
        )
        consumer2_box.shift(RIGHT * 4 + DOWN * 1.5)
        
        consumer2_text = Text("Billing\nManager", font_size=20, color=WHITE)
        consumer2_text.move_to(consumer2_box.get_center())
        
        consumer2_label = Text("Consumer", font_size=14, color="#96CEB4")
        consumer2_label.next_to(consumer2_box, DOWN, buff=0.2)
        
        # Animate Consumer 2 appearing
        self.play(
            FadeIn(consumer2_box, scale=0.8),
            FadeIn(consumer2_text),
            run_time=1
        )
        self.play(FadeIn(consumer2_label, shift=UP * 0.3), run_time=0.5)
        
        # Arrow from Kafka to Consumer 2
        arrow3 = Arrow(
            kafka_box.get_right() + DOWN * 0.5,
            consumer2_box.get_left(),
            buff=0.1,
            color="#96CEB4",
            stroke_width=6,
            max_tip_length_to_length_ratio=0.15
        )
        
        arrow3_label = Text("billing-group", font_size=16, color="#96CEB4")
        arrow3_label.next_to(arrow3, DOWN, buff=0.1)
        
        self.play(
            GrowArrow(arrow3),
            run_time=1.2
        )
        self.play(
            FadeIn(arrow3_label, shift=DOWN * 0.2),
            run_time=0.6
        )
        self.wait(0.5)
        
        # Simulate data flow with moving dots
        # Create dots that travel along the arrows
        dot1 = Dot(color=YELLOW, radius=0.15).move_to(producer_box.get_right())
        dot2 = Dot(color=YELLOW, radius=0.15).move_to(kafka_box.get_right() + UP * 0.5)
        dot3 = Dot(color=YELLOW, radius=0.15).move_to(kafka_box.get_right() + DOWN * 0.5)
        
        # Animate data flow
        self.play(
            MoveAlongPath(dot1, arrow1),
            run_time=1.5,
            rate_func=smooth
        )
        
        # Split into two consumers
        self.play(
            MoveAlongPath(dot2, arrow2),
            MoveAlongPath(dot3, arrow3),
            run_time=1.5,
            rate_func=smooth
        )
        
        # Fade out dots
        self.play(
            FadeOut(dot1),
            FadeOut(dot2),
            FadeOut(dot3),
            run_time=0.5
        )
        
        self.wait(2)
        
        # Final message
        message = Text(
            "Event-Driven Architecture",
            font_size=36,
            color="#00D9FF",
            weight=BOLD
        )
        message.to_edge(DOWN)
        
        self.play(
            Write(message),
            run_time=1.5
        )
        
        self.wait(3)


# Command to render:
# manim -pql kafka_smooth.py KafkaFlowAnimation
# For high quality: manim -pqh kafka_smooth.py KafkaFlowAnimation
# For social media (vertical): manim -pqh --format=mp4 --media_dir=./media kafka_smooth.py KafkaFlowAnimation

