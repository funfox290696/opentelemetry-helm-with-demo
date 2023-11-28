from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

trace.set_tracer_provider(TracerProvider())

otlp_exporter = OTLPSpanExporter(endpoint="http://opentelemetry-opentelemetry-collector.monitoring.svc.cluster.local:4318/v1/traces")

span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("example_span"):
    print("Hello from OpenTelemetry")

# trace.get_tracer_provider().shutdown()
