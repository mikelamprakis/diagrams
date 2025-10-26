"""
Advanced Kafka Animation with Multiple Effects
Features:
- Pulsing effects on components
- Data packets flowing through system
- Smooth transitions
- Professional color scheme
"""

from manim import *

class KafkaAdvancedFlow(Scene):
    def construct(self):
        # Dark background
        self.camera.background_color = "#1a1a1a"
        
        # Title with gradient effect
        title = Text("Kafka Event Streaming Pipeline", font_size=42, gradient=(BLUE, TEAL))
        title.to_edge(UP, buff=0.5)
        self.play(FadeIn(title, shift=DOWN), run_time=1.5)
        self.wait(0.5)
        
        # Create all components first (invisible)
        components = self.create_components()
        
        # Animate each component appearing in sequence
        self.reveal_architecture(components)
        
        # Show data flowing through the system
        self.animate_data_flow(components)
        
        # Add explanatory notes
        self.add_annotations(components)
        
        self.wait(3)
    
    def create_components(self):
        """Create all visual components"""
        # Producer
        producer = VGroup(
            RoundedRectangle(
                width=2.2, height=1.4, corner_radius=0.15,
                fill_color="#FF6B6B", fill_opacity=0.9,
                stroke_color="#E53E3E", stroke_width=2
            ),
            Text("Checkout\nService", font_size=20, color=WHITE, weight=BOLD)
        )
        producer[1].move_to(producer[0].get_center())
        producer.shift(LEFT * 4.5)
        
        # Kafka Cluster with partitions
        kafka_main = RoundedRectangle(
            width=3.5, height=3, corner_radius=0.2,
            fill_color="#2C3E50", fill_opacity=0.95,
            stroke_color="#3498DB", stroke_width=3
        )
        
        kafka_title = Text("Kafka Cluster", font_size=24, color="#3498DB", weight=BOLD)
        kafka_title.move_to(kafka_main.get_top() + DOWN * 0.4)
        
        # Topic name
        topic_name = Text("orders", font_size=28, color=YELLOW, weight=BOLD, slant=ITALIC)
        topic_name.move_to(kafka_main.get_center() + UP * 0.5)
        
        # Partitions
        partitions = VGroup()
        colors = ["#E74C3C", "#F39C12", "#27AE60"]
        for i in range(3):
            p = RoundedRectangle(
                width=0.8, height=0.4, corner_radius=0.1,
                fill_color=colors[i], fill_opacity=0.7,
                stroke_color=colors[i], stroke_width=2
            )
            p_text = Text(f"P{i}", font_size=14, color=WHITE)
            p_text.move_to(p.get_center())
            p_group = VGroup(p, p_text)
            p_group.shift(LEFT * 1 + RIGHT * i * 0.9 + DOWN * 0.6)
            partitions.add(p_group)
        
        kafka = VGroup(kafka_main, kafka_title, topic_name, partitions)
        
        # Consumers
        consumer1 = VGroup(
            RoundedRectangle(
                width=2.2, height=1.4, corner_radius=0.15,
                fill_color="#4ECDC4", fill_opacity=0.9,
                stroke_color="#38B2AC", stroke_width=2
            ),
            Text("Inventory\nManager", font_size=18, color=WHITE, weight=BOLD)
        )
        consumer1[1].move_to(consumer1[0].get_center())
        consumer1.shift(RIGHT * 4.5 + UP * 1.3)
        
        consumer2 = VGroup(
            RoundedRectangle(
                width=2.2, height=1.4, corner_radius=0.15,
                fill_color="#96CEB4", fill_opacity=0.9,
                stroke_color="#68D391", stroke_width=2
            ),
            Text("Billing\nManager", font_size=18, color=WHITE, weight=BOLD)
        )
        consumer2[1].move_to(consumer2[0].get_center())
        consumer2.shift(RIGHT * 4.5 + DOWN * 1.3)
        
        return {
            "producer": producer,
            "kafka": kafka,
            "consumer1": consumer1,
            "consumer2": consumer2
        }
    
    def reveal_architecture(self, components):
        """Animate components appearing in sequence"""
        # Producer appears
        self.play(
            FadeIn(components["producer"], scale=0.7),
            run_time=1.2
        )
        
        # Add pulsing effect to producer
        self.play(
            components["producer"][0].animate.set_fill(opacity=1).scale(1.1),
            rate_func=there_and_back,
            run_time=0.8
        )
        self.wait(0.3)
        
        # Kafka cluster appears
        self.play(
            FadeIn(components["kafka"][0:3], scale=0.7),
            run_time=1.2
        )
        
        # Partitions appear one by one
        for partition in components["kafka"][3]:
            self.play(
                FadeIn(partition, shift=DOWN * 0.3),
                run_time=0.4
            )
        self.wait(0.3)
        
        # Consumers appear
        self.play(
            FadeIn(components["consumer1"], scale=0.7, shift=LEFT * 0.5),
            run_time=1
        )
        self.play(
            FadeIn(components["consumer2"], scale=0.7, shift=LEFT * 0.5),
            run_time=1
        )
        self.wait(0.5)
    
    def animate_data_flow(self, components):
        """Show data flowing through the system with smooth animations"""
        # Create arrows
        arrow1 = Arrow(
            components["producer"].get_right(),
            components["kafka"][0].get_left(),
            buff=0.1, color="#00D9FF", stroke_width=5
        )
        
        arrow2 = Arrow(
            components["kafka"][0].get_right() + UP * 0.8,
            components["consumer1"].get_left(),
            buff=0.1, color="#4ECDC4", stroke_width=5
        )
        
        arrow3 = Arrow(
            components["kafka"][0].get_right() + DOWN * 0.8,
            components["consumer2"].get_left(),
            buff=0.1, color="#96CEB4", stroke_width=5
        )
        
        # Arrows grow
        self.play(
            GrowArrow(arrow1),
            run_time=1
        )
        self.play(
            GrowArrow(arrow2),
            GrowArrow(arrow3),
            run_time=1
        )
        self.wait(0.5)
        
        # Create data packets (glowing dots)
        for i in range(3):
            # Create order packet
            packet = Circle(radius=0.15, fill_color=YELLOW, fill_opacity=1, stroke_width=0)
            packet.move_to(components["producer"].get_right())
            
            # Add glow effect
            glow = Circle(radius=0.25, fill_color=YELLOW, fill_opacity=0.3, stroke_width=0)
            glow.move_to(packet.get_center())
            
            packet_group = VGroup(glow, packet)
            
            # Animate packet flowing
            self.play(
                FadeIn(packet_group, scale=0.5),
                run_time=0.3
            )
            
            # Move to Kafka
            self.play(
                packet_group.animate.move_to(components["kafka"][0].get_center()),
                run_time=1,
                rate_func=smooth
            )
            
            # Pulse effect at Kafka
            self.play(
                packet_group.animate.scale(1.3),
                rate_func=there_and_back,
                run_time=0.4
            )
            
            # Split to consumers
            packet1 = packet_group.copy()
            packet2 = packet_group.copy()
            
            self.play(
                packet1.animate.move_to(components["consumer1"].get_center()),
                packet2.animate.move_to(components["consumer2"].get_center()),
                run_time=1,
                rate_func=smooth
            )
            
            # Fade out at consumers
            self.play(
                FadeOut(packet_group),
                FadeOut(packet1, scale=1.5),
                FadeOut(packet2, scale=1.5),
                run_time=0.5
            )
            
            self.wait(0.2)
    
    def add_annotations(self, components):
        """Add explanatory notes"""
        note = Text(
            "Scalable • Fault-Tolerant • Real-Time",
            font_size=24,
            color="#00D9FF",
            slant=ITALIC
        )
        note.to_edge(DOWN, buff=0.5)
        
        self.play(
            Write(note),
            run_time=2
        )


# Render commands:
# Low quality preview: manim -pql kafka_advanced.py KafkaAdvancedFlow
# High quality: manim -pqh kafka_advanced.py KafkaAdvancedFlow  
# 1080p vertical (Reels/TikTok): manim -pqh -r 1080,1920 kafka_advanced.py KafkaAdvancedFlow
# 1080p square (Instagram): manim -pqh -r 1080,1080 kafka_advanced.py KafkaAdvancedFlow

