from sqlalchemy import Column, Numeric, Enum, String, ForeignKey, DateTime
from whitebox.entities.Base import Base
from sqlalchemy.orm import relationship
from whitebox.schemas.modelMonitor import AlertSeverity, MonitorMetrics, MonitorStatus
from whitebox.utils.id_gen import generate_uuid


class ModelMonitor(Base):
    __tablename__ = "model_monitors"

    id = Column(String, primary_key=True, unique=True, default=generate_uuid)
    model_id = Column(String, ForeignKey("models.id", ondelete="CASCADE"))
    name = Column(String)
    status = Column("status", Enum(MonitorStatus))
    metric = Column("metric", Enum(MonitorMetrics))
    feature = Column(String, nullable=True)
    lower_threshold = Column(Numeric, nullable=True)
    severity = Column("severity", Enum(AlertSeverity))
    email = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    alerts = relationship("Alert")
