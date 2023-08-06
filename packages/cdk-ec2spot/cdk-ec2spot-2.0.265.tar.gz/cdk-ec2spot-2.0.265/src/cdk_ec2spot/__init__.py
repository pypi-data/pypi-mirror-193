'''
[![NPM version](https://badge.fury.io/js/cdk-ec2spot.svg)](https://badge.fury.io/js/cdk-ec2spot)
[![PyPI version](https://badge.fury.io/py/cdk-ec2spot.svg)](https://badge.fury.io/py/cdk-ec2spot)
![Release](https://github.com/pahud/cdk-ec2spot/workflows/Release/badge.svg)

# `cdk-ec2spot`

CDK construct library that allows you to create EC2 Spot instances with `AWS AutoScaling Group`, `Spot Fleet` or just single `Spot Instance`.

# Install

Use the npm dist tag to opt in CDKv1 or CDKv2:

```sh
// for CDKv2
npm install cdk-ec2spot
or
npm install cdk-ec2spot@latest

// for CDKv1
npm install cdk-ec2spot@cdkv1
```

# Sample

```python
import * as ec2spot from 'cdk-ec2spot';

// create a ec2spot provider
const provider = new ec2spot.Provider(stack, 'Provider');

// import or create a vpc
const vpc = provider.getOrCreateVpc(stack);

// create an AutoScalingGroup with Launch Template for spot instances
provider.createAutoScalingGroup('SpotASG', {
  vpc,
  defaultCapacitySize: 2,
  instanceType: new ec2.InstanceType('m5.large'),
});
```

# EC2 Spot Fleet support

In addition to EC2 AutoScaling Group, you may use `createFleet()` to create an EC2 Spot Fleet:

```python
provider.createFleet('SpotFleet', {
  vpc,
  defaultCapacitySize: 2,
  instanceType: new ec2.InstanceType('t3.large'),
});
```

# Single Spot Instnce

If you just need single spot instance without any autoscaling group or spot fleet, use `createInstance()`:

```python
provider.createInstance('SpotInstance', { vpc })
```
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import aws_cdk.aws_autoscaling as _aws_cdk_aws_autoscaling_ceddda9d
import aws_cdk.aws_ec2 as _aws_cdk_aws_ec2_ceddda9d
import aws_cdk.aws_iam as _aws_cdk_aws_iam_ceddda9d
import cdk_spot_one as _cdk_spot_one_dd04be8a
import constructs as _constructs_77d1e7e8


@jsii.enum(jsii_type="cdk-ec2spot.BlockDurationMinutes")
class BlockDurationMinutes(enum.Enum):
    ONE_HOUR = "ONE_HOUR"
    TWO_HOURS = "TWO_HOURS"
    THREE_HOURS = "THREE_HOURS"
    FOUR_HOURS = "FOUR_HOURS"
    FIVE_HOURS = "FIVE_HOURS"
    SIX_HOURS = "SIX_HOURS"


@jsii.enum(jsii_type="cdk-ec2spot.InstanceInterruptionBehavior")
class InstanceInterruptionBehavior(enum.Enum):
    HIBERNATE = "HIBERNATE"
    STOP = "STOP"
    TERMINATE = "TERMINATE"


@jsii.data_type(
    jsii_type="cdk-ec2spot.LaunchTemplateOptions",
    jsii_struct_bases=[],
    name_mapping={
        "instance_profile": "instanceProfile",
        "instance_type": "instanceType",
        "machine_image": "machineImage",
        "spot_options": "spotOptions",
        "user_data": "userData",
    },
)
class LaunchTemplateOptions:
    def __init__(
        self,
        *,
        instance_profile: typing.Optional[_aws_cdk_aws_iam_ceddda9d.CfnInstanceProfile] = None,
        instance_type: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.InstanceType] = None,
        machine_image: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IMachineImage] = None,
        spot_options: typing.Optional[typing.Union["SpotOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        user_data: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.UserData] = None,
    ) -> None:
        '''
        :param instance_profile: 
        :param instance_type: 
        :param machine_image: 
        :param spot_options: 
        :param user_data: 
        '''
        if isinstance(spot_options, dict):
            spot_options = SpotOptions(**spot_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78c5694463c7660a1bf299dd53edef0853cb5e71747d612f252bbe6751f6ab09)
            check_type(argname="argument instance_profile", value=instance_profile, expected_type=type_hints["instance_profile"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument machine_image", value=machine_image, expected_type=type_hints["machine_image"])
            check_type(argname="argument spot_options", value=spot_options, expected_type=type_hints["spot_options"])
            check_type(argname="argument user_data", value=user_data, expected_type=type_hints["user_data"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if instance_profile is not None:
            self._values["instance_profile"] = instance_profile
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if machine_image is not None:
            self._values["machine_image"] = machine_image
        if spot_options is not None:
            self._values["spot_options"] = spot_options
        if user_data is not None:
            self._values["user_data"] = user_data

    @builtins.property
    def instance_profile(
        self,
    ) -> typing.Optional[_aws_cdk_aws_iam_ceddda9d.CfnInstanceProfile]:
        result = self._values.get("instance_profile")
        return typing.cast(typing.Optional[_aws_cdk_aws_iam_ceddda9d.CfnInstanceProfile], result)

    @builtins.property
    def instance_type(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.InstanceType]:
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.InstanceType], result)

    @builtins.property
    def machine_image(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IMachineImage]:
        result = self._values.get("machine_image")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IMachineImage], result)

    @builtins.property
    def spot_options(self) -> typing.Optional["SpotOptions"]:
        result = self._values.get("spot_options")
        return typing.cast(typing.Optional["SpotOptions"], result)

    @builtins.property
    def user_data(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.UserData]:
        result = self._values.get("user_data")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.UserData], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Provider(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-ec2spot.Provider",
):
    def __init__(self, scope: _constructs_77d1e7e8.Construct, id: builtins.str) -> None:
        '''
        :param scope: -
        :param id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0084407373686a8a72be599b128cde51292a4405581e5d7d1c7773a65a63a802)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        jsii.create(self.__class__, self, [scope, id])

    @jsii.member(jsii_name="createAutoScalingGroup")
    def create_auto_scaling_group(
        self,
        id: builtins.str,
        *,
        vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
        default_capacity_size: typing.Optional[jsii.Number] = None,
        instance_profile: typing.Optional[_aws_cdk_aws_iam_ceddda9d.CfnInstanceProfile] = None,
        instance_type: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.InstanceType] = None,
        machine_image: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IMachineImage] = None,
        spot_options: typing.Optional[typing.Union["SpotOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        user_data: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.UserData] = None,
    ) -> _aws_cdk_aws_autoscaling_ceddda9d.AutoScalingGroup:
        '''Create AutoScaling Group.

        :param id: AutoScaling Group ID.
        :param vpc: The vpc for the AutoScalingGroup.
        :param default_capacity_size: default capacity size for the Auto Scaling Group. Default: 1
        :param instance_profile: 
        :param instance_type: 
        :param machine_image: 
        :param spot_options: 
        :param user_data: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3566640cbc802f982a0d4a96bb0b3267e1b9cf4b46247833afc110e8d1b4cdbe)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = AutoScalingGroupOptions(
            vpc=vpc,
            default_capacity_size=default_capacity_size,
            instance_profile=instance_profile,
            instance_type=instance_type,
            machine_image=machine_image,
            spot_options=spot_options,
            user_data=user_data,
        )

        return typing.cast(_aws_cdk_aws_autoscaling_ceddda9d.AutoScalingGroup, jsii.invoke(self, "createAutoScalingGroup", [id, options]))

    @jsii.member(jsii_name="createFleet")
    def create_fleet(
        self,
        id: builtins.str,
        *,
        terminate_instances_with_expiration: typing.Optional[builtins.bool] = None,
        valid_from: typing.Optional[builtins.str] = None,
        valid_until: typing.Optional[builtins.str] = None,
        vpc_subnet: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
        vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
        default_capacity_size: typing.Optional[jsii.Number] = None,
        instance_profile: typing.Optional[_aws_cdk_aws_iam_ceddda9d.CfnInstanceProfile] = None,
        instance_type: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.InstanceType] = None,
        machine_image: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IMachineImage] = None,
        spot_options: typing.Optional[typing.Union["SpotOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        user_data: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.UserData] = None,
    ) -> _aws_cdk_aws_ec2_ceddda9d.CfnSpotFleet:
        '''Create EC2 Spot Fleet.

        :param id: fleet id.
        :param terminate_instances_with_expiration: Whether to terminate the fleet with expiration. Default: true
        :param valid_from: The timestamp of the beginning of the valid duration. Default: - now
        :param valid_until: The timestamp of the beginning of the valid duration. Default: - unlimited
        :param vpc_subnet: VPC subnet selection. Default: ec2.SubnetType.PRIVATE
        :param vpc: The vpc for the AutoScalingGroup.
        :param default_capacity_size: default capacity size for the Auto Scaling Group. Default: 1
        :param instance_profile: 
        :param instance_type: 
        :param machine_image: 
        :param spot_options: 
        :param user_data: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e928ee8d54727c94e6a91bef6df4107595145ad0f8fd6eef4fab296eeeeac06)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = SpotFleetOptions(
            terminate_instances_with_expiration=terminate_instances_with_expiration,
            valid_from=valid_from,
            valid_until=valid_until,
            vpc_subnet=vpc_subnet,
            vpc=vpc,
            default_capacity_size=default_capacity_size,
            instance_profile=instance_profile,
            instance_type=instance_type,
            machine_image=machine_image,
            spot_options=spot_options,
            user_data=user_data,
        )

        return typing.cast(_aws_cdk_aws_ec2_ceddda9d.CfnSpotFleet, jsii.invoke(self, "createFleet", [id, options]))

    @jsii.member(jsii_name="createInstance")
    def create_instance(
        self,
        id: builtins.str,
        *,
        block_device_mappings: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_ec2_ceddda9d.CfnLaunchTemplate.BlockDeviceMappingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        additional_user_data: typing.Optional[typing.Sequence[builtins.str]] = None,
        assign_eip: typing.Optional[builtins.bool] = None,
        custom_ami_id: typing.Optional[builtins.str] = None,
        default_instance_type: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.InstanceType] = None,
        ebs_volume_size: typing.Optional[jsii.Number] = None,
        eip_allocation_id: typing.Optional[builtins.str] = None,
        instance_interruption_behavior: typing.Optional[_cdk_spot_one_dd04be8a.InstanceInterruptionBehavior] = None,
        instance_profile: typing.Optional[_aws_cdk_aws_iam_ceddda9d.CfnInstanceProfile] = None,
        instance_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        key_name: typing.Optional[builtins.str] = None,
        security_group: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.SecurityGroup] = None,
        target_capacity: typing.Optional[jsii.Number] = None,
        vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
        vpc_subnet: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> _cdk_spot_one_dd04be8a.SpotInstance:
        '''
        :param id: -
        :param block_device_mappings: blockDeviceMappings for config instance. Default: - from ami config.
        :param additional_user_data: Additional commands for user data. Default: - no additional user data
        :param assign_eip: Auto assign a new EIP on this instance if ``eipAllocationId`` is not defined. Default: true
        :param custom_ami_id: custom AMI ID. Default: - The latest Amaozn Linux 2 AMI ID
        :param default_instance_type: default EC2 instance type. Default: - t3.large
        :param ebs_volume_size: default EBS volume size for the spot instance. Default: 60;
        :param eip_allocation_id: Allocation ID for your existing Elastic IP Address.
        :param instance_interruption_behavior: The behavior when a Spot Instance is interrupted. Default: - InstanceInterruptionBehavior.TERMINATE
        :param instance_profile: instance profile for the resource. Default: - create a new one
        :param instance_role: IAM role for the spot instance.
        :param key_name: SSH key name. Default: - no ssh key will be assigned
        :param security_group: Security group for the spot fleet. Default: - allows TCP 22 SSH ingress rule
        :param target_capacity: number of the target capacity. Default: - 1
        :param vpc: VPC for the spot fleet. Default: - new VPC will be created
        :param vpc_subnet: VPC subnet for the spot fleet. Default: - public subnet
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b516a9f6810a4191589369f2dbbe5830ade0f075015b6226219713dcb779b5d6)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        optons = _cdk_spot_one_dd04be8a.SpotInstanceProps(
            block_device_mappings=block_device_mappings,
            additional_user_data=additional_user_data,
            assign_eip=assign_eip,
            custom_ami_id=custom_ami_id,
            default_instance_type=default_instance_type,
            ebs_volume_size=ebs_volume_size,
            eip_allocation_id=eip_allocation_id,
            instance_interruption_behavior=instance_interruption_behavior,
            instance_profile=instance_profile,
            instance_role=instance_role,
            key_name=key_name,
            security_group=security_group,
            target_capacity=target_capacity,
            vpc=vpc,
            vpc_subnet=vpc_subnet,
        )

        return typing.cast(_cdk_spot_one_dd04be8a.SpotInstance, jsii.invoke(self, "createInstance", [id, optons]))

    @jsii.member(jsii_name="createInstanceProfile")
    def create_instance_profile(
        self,
        id: builtins.str,
    ) -> _aws_cdk_aws_iam_ceddda9d.CfnInstanceProfile:
        '''
        :param id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d353190783597c3682594ef7c0b7cf17a9dc04d8a279f795a99a134a2827ab71)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.CfnInstanceProfile, jsii.invoke(self, "createInstanceProfile", [id]))

    @jsii.member(jsii_name="createLaunchTemplate")
    def create_launch_template(
        self,
        id: builtins.str,
        *,
        instance_profile: typing.Optional[_aws_cdk_aws_iam_ceddda9d.CfnInstanceProfile] = None,
        instance_type: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.InstanceType] = None,
        machine_image: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IMachineImage] = None,
        spot_options: typing.Optional[typing.Union["SpotOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        user_data: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.UserData] = None,
    ) -> _aws_cdk_aws_ec2_ceddda9d.CfnLaunchTemplate:
        '''Create Launch Template.

        :param id: launch template id.
        :param instance_profile: 
        :param instance_type: 
        :param machine_image: 
        :param spot_options: 
        :param user_data: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7b657887259e7f17d85ad09bf8a9a9d615d1fafeb14ca39192a46d0cbc5f7b8)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = LaunchTemplateOptions(
            instance_profile=instance_profile,
            instance_type=instance_type,
            machine_image=machine_image,
            spot_options=spot_options,
            user_data=user_data,
        )

        return typing.cast(_aws_cdk_aws_ec2_ceddda9d.CfnLaunchTemplate, jsii.invoke(self, "createLaunchTemplate", [id, options]))

    @jsii.member(jsii_name="getOrCreateVpc")
    def get_or_create_vpc(
        self,
        scope: _constructs_77d1e7e8.Construct,
    ) -> _aws_cdk_aws_ec2_ceddda9d.IVpc:
        '''
        :param scope: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f809737a45dc2605ea95c217b52d1b7273144171c5409566e2f3a48cbc7279d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(_aws_cdk_aws_ec2_ceddda9d.IVpc, jsii.invoke(self, "getOrCreateVpc", [scope]))

    @builtins.property
    @jsii.member(jsii_name="amazonLinuxAmiImageId")
    def amazon_linux_ami_image_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "amazonLinuxAmiImageId"))


@jsii.enum(jsii_type="cdk-ec2spot.SpotInstanceType")
class SpotInstanceType(enum.Enum):
    ONE_TIME = "ONE_TIME"
    PERSISTENT = "PERSISTENT"


@jsii.data_type(
    jsii_type="cdk-ec2spot.SpotOptions",
    jsii_struct_bases=[],
    name_mapping={
        "block_duration_minutes": "blockDurationMinutes",
        "instance_interruption_behavior": "instanceInterruptionBehavior",
        "max_price": "maxPrice",
        "spot_instance_type": "spotInstanceType",
        "valid_until": "validUntil",
    },
)
class SpotOptions:
    def __init__(
        self,
        *,
        block_duration_minutes: typing.Optional[BlockDurationMinutes] = None,
        instance_interruption_behavior: typing.Optional[InstanceInterruptionBehavior] = None,
        max_price: typing.Optional[builtins.str] = None,
        spot_instance_type: typing.Optional[SpotInstanceType] = None,
        valid_until: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param block_duration_minutes: 
        :param instance_interruption_behavior: 
        :param max_price: 
        :param spot_instance_type: 
        :param valid_until: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae9508dd1b7712e4aa8613f6e6099edd85ce95aa1f65229913f8a4001839b7f8)
            check_type(argname="argument block_duration_minutes", value=block_duration_minutes, expected_type=type_hints["block_duration_minutes"])
            check_type(argname="argument instance_interruption_behavior", value=instance_interruption_behavior, expected_type=type_hints["instance_interruption_behavior"])
            check_type(argname="argument max_price", value=max_price, expected_type=type_hints["max_price"])
            check_type(argname="argument spot_instance_type", value=spot_instance_type, expected_type=type_hints["spot_instance_type"])
            check_type(argname="argument valid_until", value=valid_until, expected_type=type_hints["valid_until"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if block_duration_minutes is not None:
            self._values["block_duration_minutes"] = block_duration_minutes
        if instance_interruption_behavior is not None:
            self._values["instance_interruption_behavior"] = instance_interruption_behavior
        if max_price is not None:
            self._values["max_price"] = max_price
        if spot_instance_type is not None:
            self._values["spot_instance_type"] = spot_instance_type
        if valid_until is not None:
            self._values["valid_until"] = valid_until

    @builtins.property
    def block_duration_minutes(self) -> typing.Optional[BlockDurationMinutes]:
        result = self._values.get("block_duration_minutes")
        return typing.cast(typing.Optional[BlockDurationMinutes], result)

    @builtins.property
    def instance_interruption_behavior(
        self,
    ) -> typing.Optional[InstanceInterruptionBehavior]:
        result = self._values.get("instance_interruption_behavior")
        return typing.cast(typing.Optional[InstanceInterruptionBehavior], result)

    @builtins.property
    def max_price(self) -> typing.Optional[builtins.str]:
        result = self._values.get("max_price")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spot_instance_type(self) -> typing.Optional[SpotInstanceType]:
        result = self._values.get("spot_instance_type")
        return typing.cast(typing.Optional[SpotInstanceType], result)

    @builtins.property
    def valid_until(self) -> typing.Optional[builtins.str]:
        result = self._values.get("valid_until")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpotOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-ec2spot.AutoScalingGroupOptions",
    jsii_struct_bases=[LaunchTemplateOptions],
    name_mapping={
        "instance_profile": "instanceProfile",
        "instance_type": "instanceType",
        "machine_image": "machineImage",
        "spot_options": "spotOptions",
        "user_data": "userData",
        "vpc": "vpc",
        "default_capacity_size": "defaultCapacitySize",
    },
)
class AutoScalingGroupOptions(LaunchTemplateOptions):
    def __init__(
        self,
        *,
        instance_profile: typing.Optional[_aws_cdk_aws_iam_ceddda9d.CfnInstanceProfile] = None,
        instance_type: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.InstanceType] = None,
        machine_image: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IMachineImage] = None,
        spot_options: typing.Optional[typing.Union[SpotOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        user_data: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.UserData] = None,
        vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
        default_capacity_size: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param instance_profile: 
        :param instance_type: 
        :param machine_image: 
        :param spot_options: 
        :param user_data: 
        :param vpc: The vpc for the AutoScalingGroup.
        :param default_capacity_size: default capacity size for the Auto Scaling Group. Default: 1
        '''
        if isinstance(spot_options, dict):
            spot_options = SpotOptions(**spot_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59b1dd8d3301a15069c69deac346d143286429af8f0aa09e38100294c49388c3)
            check_type(argname="argument instance_profile", value=instance_profile, expected_type=type_hints["instance_profile"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument machine_image", value=machine_image, expected_type=type_hints["machine_image"])
            check_type(argname="argument spot_options", value=spot_options, expected_type=type_hints["spot_options"])
            check_type(argname="argument user_data", value=user_data, expected_type=type_hints["user_data"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument default_capacity_size", value=default_capacity_size, expected_type=type_hints["default_capacity_size"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vpc": vpc,
        }
        if instance_profile is not None:
            self._values["instance_profile"] = instance_profile
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if machine_image is not None:
            self._values["machine_image"] = machine_image
        if spot_options is not None:
            self._values["spot_options"] = spot_options
        if user_data is not None:
            self._values["user_data"] = user_data
        if default_capacity_size is not None:
            self._values["default_capacity_size"] = default_capacity_size

    @builtins.property
    def instance_profile(
        self,
    ) -> typing.Optional[_aws_cdk_aws_iam_ceddda9d.CfnInstanceProfile]:
        result = self._values.get("instance_profile")
        return typing.cast(typing.Optional[_aws_cdk_aws_iam_ceddda9d.CfnInstanceProfile], result)

    @builtins.property
    def instance_type(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.InstanceType]:
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.InstanceType], result)

    @builtins.property
    def machine_image(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IMachineImage]:
        result = self._values.get("machine_image")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IMachineImage], result)

    @builtins.property
    def spot_options(self) -> typing.Optional[SpotOptions]:
        result = self._values.get("spot_options")
        return typing.cast(typing.Optional[SpotOptions], result)

    @builtins.property
    def user_data(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.UserData]:
        result = self._values.get("user_data")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.UserData], result)

    @builtins.property
    def vpc(self) -> _aws_cdk_aws_ec2_ceddda9d.IVpc:
        '''The vpc for the AutoScalingGroup.'''
        result = self._values.get("vpc")
        assert result is not None, "Required property 'vpc' is missing"
        return typing.cast(_aws_cdk_aws_ec2_ceddda9d.IVpc, result)

    @builtins.property
    def default_capacity_size(self) -> typing.Optional[jsii.Number]:
        '''default capacity size for the Auto Scaling Group.

        :default: 1
        '''
        result = self._values.get("default_capacity_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoScalingGroupOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-ec2spot.SpotFleetOptions",
    jsii_struct_bases=[AutoScalingGroupOptions],
    name_mapping={
        "instance_profile": "instanceProfile",
        "instance_type": "instanceType",
        "machine_image": "machineImage",
        "spot_options": "spotOptions",
        "user_data": "userData",
        "vpc": "vpc",
        "default_capacity_size": "defaultCapacitySize",
        "terminate_instances_with_expiration": "terminateInstancesWithExpiration",
        "valid_from": "validFrom",
        "valid_until": "validUntil",
        "vpc_subnet": "vpcSubnet",
    },
)
class SpotFleetOptions(AutoScalingGroupOptions):
    def __init__(
        self,
        *,
        instance_profile: typing.Optional[_aws_cdk_aws_iam_ceddda9d.CfnInstanceProfile] = None,
        instance_type: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.InstanceType] = None,
        machine_image: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IMachineImage] = None,
        spot_options: typing.Optional[typing.Union[SpotOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        user_data: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.UserData] = None,
        vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
        default_capacity_size: typing.Optional[jsii.Number] = None,
        terminate_instances_with_expiration: typing.Optional[builtins.bool] = None,
        valid_from: typing.Optional[builtins.str] = None,
        valid_until: typing.Optional[builtins.str] = None,
        vpc_subnet: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param instance_profile: 
        :param instance_type: 
        :param machine_image: 
        :param spot_options: 
        :param user_data: 
        :param vpc: The vpc for the AutoScalingGroup.
        :param default_capacity_size: default capacity size for the Auto Scaling Group. Default: 1
        :param terminate_instances_with_expiration: Whether to terminate the fleet with expiration. Default: true
        :param valid_from: The timestamp of the beginning of the valid duration. Default: - now
        :param valid_until: The timestamp of the beginning of the valid duration. Default: - unlimited
        :param vpc_subnet: VPC subnet selection. Default: ec2.SubnetType.PRIVATE
        '''
        if isinstance(spot_options, dict):
            spot_options = SpotOptions(**spot_options)
        if isinstance(vpc_subnet, dict):
            vpc_subnet = _aws_cdk_aws_ec2_ceddda9d.SubnetSelection(**vpc_subnet)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0805845bdc6545defca9fbcf4d117953ddd60be3e05b25bb8c71ceb7fccd6444)
            check_type(argname="argument instance_profile", value=instance_profile, expected_type=type_hints["instance_profile"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument machine_image", value=machine_image, expected_type=type_hints["machine_image"])
            check_type(argname="argument spot_options", value=spot_options, expected_type=type_hints["spot_options"])
            check_type(argname="argument user_data", value=user_data, expected_type=type_hints["user_data"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument default_capacity_size", value=default_capacity_size, expected_type=type_hints["default_capacity_size"])
            check_type(argname="argument terminate_instances_with_expiration", value=terminate_instances_with_expiration, expected_type=type_hints["terminate_instances_with_expiration"])
            check_type(argname="argument valid_from", value=valid_from, expected_type=type_hints["valid_from"])
            check_type(argname="argument valid_until", value=valid_until, expected_type=type_hints["valid_until"])
            check_type(argname="argument vpc_subnet", value=vpc_subnet, expected_type=type_hints["vpc_subnet"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vpc": vpc,
        }
        if instance_profile is not None:
            self._values["instance_profile"] = instance_profile
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if machine_image is not None:
            self._values["machine_image"] = machine_image
        if spot_options is not None:
            self._values["spot_options"] = spot_options
        if user_data is not None:
            self._values["user_data"] = user_data
        if default_capacity_size is not None:
            self._values["default_capacity_size"] = default_capacity_size
        if terminate_instances_with_expiration is not None:
            self._values["terminate_instances_with_expiration"] = terminate_instances_with_expiration
        if valid_from is not None:
            self._values["valid_from"] = valid_from
        if valid_until is not None:
            self._values["valid_until"] = valid_until
        if vpc_subnet is not None:
            self._values["vpc_subnet"] = vpc_subnet

    @builtins.property
    def instance_profile(
        self,
    ) -> typing.Optional[_aws_cdk_aws_iam_ceddda9d.CfnInstanceProfile]:
        result = self._values.get("instance_profile")
        return typing.cast(typing.Optional[_aws_cdk_aws_iam_ceddda9d.CfnInstanceProfile], result)

    @builtins.property
    def instance_type(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.InstanceType]:
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.InstanceType], result)

    @builtins.property
    def machine_image(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IMachineImage]:
        result = self._values.get("machine_image")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IMachineImage], result)

    @builtins.property
    def spot_options(self) -> typing.Optional[SpotOptions]:
        result = self._values.get("spot_options")
        return typing.cast(typing.Optional[SpotOptions], result)

    @builtins.property
    def user_data(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.UserData]:
        result = self._values.get("user_data")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.UserData], result)

    @builtins.property
    def vpc(self) -> _aws_cdk_aws_ec2_ceddda9d.IVpc:
        '''The vpc for the AutoScalingGroup.'''
        result = self._values.get("vpc")
        assert result is not None, "Required property 'vpc' is missing"
        return typing.cast(_aws_cdk_aws_ec2_ceddda9d.IVpc, result)

    @builtins.property
    def default_capacity_size(self) -> typing.Optional[jsii.Number]:
        '''default capacity size for the Auto Scaling Group.

        :default: 1
        '''
        result = self._values.get("default_capacity_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def terminate_instances_with_expiration(self) -> typing.Optional[builtins.bool]:
        '''Whether to terminate the fleet with expiration.

        :default: true
        '''
        result = self._values.get("terminate_instances_with_expiration")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def valid_from(self) -> typing.Optional[builtins.str]:
        '''The timestamp of the beginning of the valid duration.

        :default: - now
        '''
        result = self._values.get("valid_from")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def valid_until(self) -> typing.Optional[builtins.str]:
        '''The timestamp of the beginning of the valid duration.

        :default: - unlimited
        '''
        result = self._values.get("valid_until")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_subnet(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection]:
        '''VPC subnet selection.

        :default: ec2.SubnetType.PRIVATE
        '''
        result = self._values.get("vpc_subnet")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpotFleetOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AutoScalingGroupOptions",
    "BlockDurationMinutes",
    "InstanceInterruptionBehavior",
    "LaunchTemplateOptions",
    "Provider",
    "SpotFleetOptions",
    "SpotInstanceType",
    "SpotOptions",
]

publication.publish()

def _typecheckingstub__78c5694463c7660a1bf299dd53edef0853cb5e71747d612f252bbe6751f6ab09(
    *,
    instance_profile: typing.Optional[_aws_cdk_aws_iam_ceddda9d.CfnInstanceProfile] = None,
    instance_type: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.InstanceType] = None,
    machine_image: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IMachineImage] = None,
    spot_options: typing.Optional[typing.Union[SpotOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    user_data: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.UserData] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0084407373686a8a72be599b128cde51292a4405581e5d7d1c7773a65a63a802(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3566640cbc802f982a0d4a96bb0b3267e1b9cf4b46247833afc110e8d1b4cdbe(
    id: builtins.str,
    *,
    vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
    default_capacity_size: typing.Optional[jsii.Number] = None,
    instance_profile: typing.Optional[_aws_cdk_aws_iam_ceddda9d.CfnInstanceProfile] = None,
    instance_type: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.InstanceType] = None,
    machine_image: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IMachineImage] = None,
    spot_options: typing.Optional[typing.Union[SpotOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    user_data: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.UserData] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e928ee8d54727c94e6a91bef6df4107595145ad0f8fd6eef4fab296eeeeac06(
    id: builtins.str,
    *,
    terminate_instances_with_expiration: typing.Optional[builtins.bool] = None,
    valid_from: typing.Optional[builtins.str] = None,
    valid_until: typing.Optional[builtins.str] = None,
    vpc_subnet: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
    vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
    default_capacity_size: typing.Optional[jsii.Number] = None,
    instance_profile: typing.Optional[_aws_cdk_aws_iam_ceddda9d.CfnInstanceProfile] = None,
    instance_type: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.InstanceType] = None,
    machine_image: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IMachineImage] = None,
    spot_options: typing.Optional[typing.Union[SpotOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    user_data: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.UserData] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b516a9f6810a4191589369f2dbbe5830ade0f075015b6226219713dcb779b5d6(
    id: builtins.str,
    *,
    block_device_mappings: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_ec2_ceddda9d.CfnLaunchTemplate.BlockDeviceMappingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    additional_user_data: typing.Optional[typing.Sequence[builtins.str]] = None,
    assign_eip: typing.Optional[builtins.bool] = None,
    custom_ami_id: typing.Optional[builtins.str] = None,
    default_instance_type: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.InstanceType] = None,
    ebs_volume_size: typing.Optional[jsii.Number] = None,
    eip_allocation_id: typing.Optional[builtins.str] = None,
    instance_interruption_behavior: typing.Optional[_cdk_spot_one_dd04be8a.InstanceInterruptionBehavior] = None,
    instance_profile: typing.Optional[_aws_cdk_aws_iam_ceddda9d.CfnInstanceProfile] = None,
    instance_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    key_name: typing.Optional[builtins.str] = None,
    security_group: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.SecurityGroup] = None,
    target_capacity: typing.Optional[jsii.Number] = None,
    vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
    vpc_subnet: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d353190783597c3682594ef7c0b7cf17a9dc04d8a279f795a99a134a2827ab71(
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7b657887259e7f17d85ad09bf8a9a9d615d1fafeb14ca39192a46d0cbc5f7b8(
    id: builtins.str,
    *,
    instance_profile: typing.Optional[_aws_cdk_aws_iam_ceddda9d.CfnInstanceProfile] = None,
    instance_type: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.InstanceType] = None,
    machine_image: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IMachineImage] = None,
    spot_options: typing.Optional[typing.Union[SpotOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    user_data: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.UserData] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f809737a45dc2605ea95c217b52d1b7273144171c5409566e2f3a48cbc7279d(
    scope: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae9508dd1b7712e4aa8613f6e6099edd85ce95aa1f65229913f8a4001839b7f8(
    *,
    block_duration_minutes: typing.Optional[BlockDurationMinutes] = None,
    instance_interruption_behavior: typing.Optional[InstanceInterruptionBehavior] = None,
    max_price: typing.Optional[builtins.str] = None,
    spot_instance_type: typing.Optional[SpotInstanceType] = None,
    valid_until: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59b1dd8d3301a15069c69deac346d143286429af8f0aa09e38100294c49388c3(
    *,
    instance_profile: typing.Optional[_aws_cdk_aws_iam_ceddda9d.CfnInstanceProfile] = None,
    instance_type: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.InstanceType] = None,
    machine_image: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IMachineImage] = None,
    spot_options: typing.Optional[typing.Union[SpotOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    user_data: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.UserData] = None,
    vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
    default_capacity_size: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0805845bdc6545defca9fbcf4d117953ddd60be3e05b25bb8c71ceb7fccd6444(
    *,
    instance_profile: typing.Optional[_aws_cdk_aws_iam_ceddda9d.CfnInstanceProfile] = None,
    instance_type: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.InstanceType] = None,
    machine_image: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IMachineImage] = None,
    spot_options: typing.Optional[typing.Union[SpotOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    user_data: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.UserData] = None,
    vpc: _aws_cdk_aws_ec2_ceddda9d.IVpc,
    default_capacity_size: typing.Optional[jsii.Number] = None,
    terminate_instances_with_expiration: typing.Optional[builtins.bool] = None,
    valid_from: typing.Optional[builtins.str] = None,
    valid_until: typing.Optional[builtins.str] = None,
    vpc_subnet: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass
