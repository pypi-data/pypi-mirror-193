import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

from .. import (
    Component as _Component_2b0ad27f,
    Gitpod as _Gitpod_5d9b9d87,
    LoggerOptions as _LoggerOptions_eb0f6309,
    Project as _Project_57d89203,
    ProjectOptions as _ProjectOptions_0d5b93c6,
    ProjectType as _ProjectType_fd80c725,
    ProjenrcOptions as _ProjenrcOptions_164bd039,
    RenovatebotOptions as _RenovatebotOptions_18e6b8a1,
    SampleReadmeProps as _SampleReadmeProps_3518b03b,
    Task as _Task_9fa875b6,
    TextFile as _TextFile_4a74808c,
    YamlFile as _YamlFile_909731b0,
)
from ..vscode import DevContainer as _DevContainer_ae6f3538, VsCode as _VsCode_9f0f4eb5
from .workflows import (
    AppPermissions as _AppPermissions_59709d51,
    BranchProtectionRuleOptions as _BranchProtectionRuleOptions_422f7f4e,
    CheckRunOptions as _CheckRunOptions_66af1ceb,
    CheckSuiteOptions as _CheckSuiteOptions_6a122376,
    ContainerOptions as _ContainerOptions_f50907af,
    CreateOptions as _CreateOptions_6247308d,
    CronScheduleOptions as _CronScheduleOptions_7724cd93,
    DeleteOptions as _DeleteOptions_c46578d4,
    DeploymentOptions as _DeploymentOptions_0bea6580,
    DeploymentStatusOptions as _DeploymentStatusOptions_f9cbd32b,
    DiscussionCommentOptions as _DiscussionCommentOptions_e8674c31,
    DiscussionOptions as _DiscussionOptions_6b34c7b6,
    ForkOptions as _ForkOptions_0437229d,
    GollumOptions as _GollumOptions_1acffea2,
    IssueCommentOptions as _IssueCommentOptions_b551b1e5,
    IssuesOptions as _IssuesOptions_dd89885c,
    Job as _Job_20ffcf45,
    JobCallingReusableWorkflow as _JobCallingReusableWorkflow_12ad1018,
    JobPermissions as _JobPermissions_3b5b53dc,
    JobStep as _JobStep_c3287c05,
    JobStepOutput as _JobStepOutput_acebe827,
    LabelOptions as _LabelOptions_ca474a61,
    MergeGroupOptions as _MergeGroupOptions_683d3a61,
    MilestoneOptions as _MilestoneOptions_6f9d8b6f,
    PageBuildOptions as _PageBuildOptions_c30eafce,
    ProjectCardOptions as _ProjectCardOptions_c89fc28d,
    ProjectColumnOptions as _ProjectColumnOptions_25a462f6,
    ProjectOptions as _ProjectOptions_50d963ea,
    PublicOptions as _PublicOptions_2c3a3b94,
    PullRequestOptions as _PullRequestOptions_b051b0c9,
    PullRequestReviewCommentOptions as _PullRequestReviewCommentOptions_85235a68,
    PullRequestReviewOptions as _PullRequestReviewOptions_27fd8e95,
    PullRequestTargetOptions as _PullRequestTargetOptions_81011bb1,
    PushOptions as _PushOptions_63e1c4f2,
    RegistryPackageOptions as _RegistryPackageOptions_781d5ac7,
    ReleaseOptions as _ReleaseOptions_d152186d,
    RepositoryDispatchOptions as _RepositoryDispatchOptions_d75e9903,
    StatusOptions as _StatusOptions_aa35df44,
    Triggers as _Triggers_e9ae7617,
    WatchOptions as _WatchOptions_d33f5d00,
    WorkflowCallOptions as _WorkflowCallOptions_bc57a5b4,
    WorkflowDispatchOptions as _WorkflowDispatchOptions_7110ffdc,
    WorkflowRunOptions as _WorkflowRunOptions_5a4262c5,
)


class AutoApprove(
    _Component_2b0ad27f,
    metaclass=jsii.JSIIMeta,
    jsii_type="projen.github.AutoApprove",
):
    '''(experimental) Auto approve pull requests that meet a criteria.

    :stability: experimental
    '''

    def __init__(
        self,
        github: "GitHub",
        *,
        allowed_usernames: typing.Optional[typing.Sequence[builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        runs_on: typing.Optional[typing.Sequence[builtins.str]] = None,
        secret: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param github: -
        :param allowed_usernames: (experimental) Only pull requests authored by these Github usernames will be auto-approved. Default: ['github-bot']
        :param label: (experimental) Only pull requests with this label will be auto-approved. Default: 'auto-approve'
        :param runs_on: (experimental) Github Runner selection labels. Default: ["ubuntu-latest"]
        :param secret: (experimental) A GitHub secret name which contains a GitHub Access Token with write permissions for the ``pull_request`` scope. This token is used to approve pull requests. Github forbids an identity to approve its own pull request. If your project produces automated pull requests using the Github default token - {@link https://docs.github.com/en/actions/reference/authentication-in-a-workflow ``GITHUB_TOKEN`` } - that you would like auto approved, such as when using the ``depsUpgrade`` property in ``NodeProjectOptions``, then you must use a different token here. Default: "GITHUB_TOKEN"

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9950225018303493365be2cb651e0d7d64a1e6439bed8efe63e4e98ab101e8a)
            check_type(argname="argument github", value=github, expected_type=type_hints["github"])
        options = AutoApproveOptions(
            allowed_usernames=allowed_usernames,
            label=label,
            runs_on=runs_on,
            secret=secret,
        )

        jsii.create(self.__class__, self, [github, options])

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "label"))


@jsii.data_type(
    jsii_type="projen.github.AutoApproveOptions",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_usernames": "allowedUsernames",
        "label": "label",
        "runs_on": "runsOn",
        "secret": "secret",
    },
)
class AutoApproveOptions:
    def __init__(
        self,
        *,
        allowed_usernames: typing.Optional[typing.Sequence[builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        runs_on: typing.Optional[typing.Sequence[builtins.str]] = None,
        secret: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Options for 'AutoApprove'.

        :param allowed_usernames: (experimental) Only pull requests authored by these Github usernames will be auto-approved. Default: ['github-bot']
        :param label: (experimental) Only pull requests with this label will be auto-approved. Default: 'auto-approve'
        :param runs_on: (experimental) Github Runner selection labels. Default: ["ubuntu-latest"]
        :param secret: (experimental) A GitHub secret name which contains a GitHub Access Token with write permissions for the ``pull_request`` scope. This token is used to approve pull requests. Github forbids an identity to approve its own pull request. If your project produces automated pull requests using the Github default token - {@link https://docs.github.com/en/actions/reference/authentication-in-a-workflow ``GITHUB_TOKEN`` } - that you would like auto approved, such as when using the ``depsUpgrade`` property in ``NodeProjectOptions``, then you must use a different token here. Default: "GITHUB_TOKEN"

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f9c4613bc56be10f461d808c77225c1917fcd25ebccedbc39aa410ff163ca51)
            check_type(argname="argument allowed_usernames", value=allowed_usernames, expected_type=type_hints["allowed_usernames"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument runs_on", value=runs_on, expected_type=type_hints["runs_on"])
            check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if allowed_usernames is not None:
            self._values["allowed_usernames"] = allowed_usernames
        if label is not None:
            self._values["label"] = label
        if runs_on is not None:
            self._values["runs_on"] = runs_on
        if secret is not None:
            self._values["secret"] = secret

    @builtins.property
    def allowed_usernames(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) Only pull requests authored by these Github usernames will be auto-approved.

        :default: ['github-bot']

        :stability: experimental
        '''
        result = self._values.get("allowed_usernames")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''(experimental) Only pull requests with this label will be auto-approved.

        :default: 'auto-approve'

        :stability: experimental
        '''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def runs_on(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) Github Runner selection labels.

        :default: ["ubuntu-latest"]

        :stability: experimental
        '''
        result = self._values.get("runs_on")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def secret(self) -> typing.Optional[builtins.str]:
        '''(experimental) A GitHub secret name which contains a GitHub Access Token with write permissions for the ``pull_request`` scope.

        This token is used to approve pull requests.

        Github forbids an identity to approve its own pull request.
        If your project produces automated pull requests using the Github default token -
        {@link https://docs.github.com/en/actions/reference/authentication-in-a-workflow ``GITHUB_TOKEN`` }

        - that you would like auto approved, such as when using the ``depsUpgrade`` property in
          ``NodeProjectOptions``, then you must use a different token here.

        :default: "GITHUB_TOKEN"

        :stability: experimental
        '''
        result = self._values.get("secret")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoApproveOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AutoMerge(
    _Component_2b0ad27f,
    metaclass=jsii.JSIIMeta,
    jsii_type="projen.github.AutoMerge",
):
    '''(experimental) Sets up mergify to merging approved pull requests.

    If ``buildJob`` is specified, the specified GitHub workflow job ID is required
    to succeed in order for the PR to be merged.

    ``approvedReviews`` specified the number of code review approvals required for
    the PR to be merged.

    :stability: experimental
    '''

    def __init__(
        self,
        github: "GitHub",
        *,
        approved_reviews: typing.Optional[jsii.Number] = None,
        blocking_labels: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param github: -
        :param approved_reviews: (experimental) Number of approved code reviews. Default: 1
        :param blocking_labels: (experimental) List of labels that will prevent auto-merging. Default: ['do-not-merge']

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a125392ca9d07df0a091430c42a2b3667d34352f1988581c1a676ea6b97b23ee)
            check_type(argname="argument github", value=github, expected_type=type_hints["github"])
        options = AutoMergeOptions(
            approved_reviews=approved_reviews, blocking_labels=blocking_labels
        )

        jsii.create(self.__class__, self, [github, options])

    @jsii.member(jsii_name="addConditions")
    def add_conditions(self, *conditions: builtins.str) -> None:
        '''(experimental) Adds conditions to the auto merge rule.

        :param conditions: The conditions to add (mergify syntax).

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fc6f0a71e209ec5af66ae78f6e33286352ce740d2b4f5322d49235524925962)
            check_type(argname="argument conditions", value=conditions, expected_type=typing.Tuple[type_hints["conditions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addConditions", [*conditions]))

    @jsii.member(jsii_name="addConditionsLater")
    def add_conditions_later(self, later: "IAddConditionsLater") -> None:
        '''(experimental) Adds conditions that will be rendered only during synthesis.

        :param later: The later.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d31a0b1fd99df9d992f0152c47af38a540e5f5ced1936de9b0aa46f305ec5355)
            check_type(argname="argument later", value=later, expected_type=type_hints["later"])
        return typing.cast(None, jsii.invoke(self, "addConditionsLater", [later]))


@jsii.data_type(
    jsii_type="projen.github.AutoMergeOptions",
    jsii_struct_bases=[],
    name_mapping={
        "approved_reviews": "approvedReviews",
        "blocking_labels": "blockingLabels",
    },
)
class AutoMergeOptions:
    def __init__(
        self,
        *,
        approved_reviews: typing.Optional[jsii.Number] = None,
        blocking_labels: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param approved_reviews: (experimental) Number of approved code reviews. Default: 1
        :param blocking_labels: (experimental) List of labels that will prevent auto-merging. Default: ['do-not-merge']

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8ab02e50aae05e5a55d4a4adc4369d19ed7205ed83b7ca13d32b3d6250e676a)
            check_type(argname="argument approved_reviews", value=approved_reviews, expected_type=type_hints["approved_reviews"])
            check_type(argname="argument blocking_labels", value=blocking_labels, expected_type=type_hints["blocking_labels"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if approved_reviews is not None:
            self._values["approved_reviews"] = approved_reviews
        if blocking_labels is not None:
            self._values["blocking_labels"] = blocking_labels

    @builtins.property
    def approved_reviews(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Number of approved code reviews.

        :default: 1

        :stability: experimental
        '''
        result = self._values.get("approved_reviews")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def blocking_labels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) List of labels that will prevent auto-merging.

        :default: ['do-not-merge']

        :stability: experimental
        '''
        result = self._values.get("blocking_labels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoMergeOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Dependabot(
    _Component_2b0ad27f,
    metaclass=jsii.JSIIMeta,
    jsii_type="projen.github.Dependabot",
):
    '''(experimental) Defines dependabot configuration for node projects.

    Since module versions are managed in projen, the versioning strategy will be
    configured to "lockfile-only" which means that only updates that can be done
    on the lockfile itself will be proposed.

    :stability: experimental
    '''

    def __init__(
        self,
        github: "GitHub",
        *,
        ignore: typing.Optional[typing.Sequence[typing.Union["DependabotIgnore", typing.Dict[builtins.str, typing.Any]]]] = None,
        ignore_projen: typing.Optional[builtins.bool] = None,
        labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        registries: typing.Optional[typing.Mapping[builtins.str, typing.Union["DependabotRegistry", typing.Dict[builtins.str, typing.Any]]]] = None,
        schedule_interval: typing.Optional["DependabotScheduleInterval"] = None,
        versioning_strategy: typing.Optional["VersioningStrategy"] = None,
    ) -> None:
        '''
        :param github: -
        :param ignore: (experimental) You can use the ``ignore`` option to customize which dependencies are updated. The ignore option supports the following options. Default: []
        :param ignore_projen: (experimental) Ignores updates to ``projen``. This is required since projen updates may cause changes in committed files and anti-tamper checks will fail. Projen upgrades are covered through the ``ProjenUpgrade`` class. Default: true
        :param labels: (experimental) List of labels to apply to the created PR's.
        :param registries: (experimental) Map of package registries to use. Default: - use public registries
        :param schedule_interval: (experimental) How often to check for new versions and raise pull requests. Default: ScheduleInterval.DAILY
        :param versioning_strategy: (experimental) The strategy to use when edits manifest and lock files. Default: VersioningStrategy.LOCKFILE_ONLY The default is to only update the lock file because package.json is controlled by projen and any outside updates will fail the build.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2caae883697ce14c090e89c8fd0dbbab7e7c0f31d6d4d66311f05a6793bd9e92)
            check_type(argname="argument github", value=github, expected_type=type_hints["github"])
        options = DependabotOptions(
            ignore=ignore,
            ignore_projen=ignore_projen,
            labels=labels,
            registries=registries,
            schedule_interval=schedule_interval,
            versioning_strategy=versioning_strategy,
        )

        jsii.create(self.__class__, self, [github, options])

    @jsii.member(jsii_name="addIgnore")
    def add_ignore(
        self,
        dependency_name: builtins.str,
        *versions: builtins.str,
    ) -> None:
        '''(experimental) Ignores a dependency from automatic updates.

        :param dependency_name: Use to ignore updates for dependencies with matching names, optionally using ``*`` to match zero or more characters.
        :param versions: Use to ignore specific versions or ranges of versions. If you want to define a range, use the standard pattern for the package manager (for example: ``^1.0.0`` for npm, or ``~> 2.0`` for Bundler).

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7691a54ace72067f7bae441e5ddeb589e23479b335d208490ece30b03e170d02)
            check_type(argname="argument dependency_name", value=dependency_name, expected_type=type_hints["dependency_name"])
            check_type(argname="argument versions", value=versions, expected_type=typing.Tuple[type_hints["versions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addIgnore", [dependency_name, *versions]))

    @builtins.property
    @jsii.member(jsii_name="config")
    def config(self) -> typing.Any:
        '''(experimental) The raw dependabot configuration.

        :see: https://docs.github.com/en/github/administering-a-repository/configuration-options-for-dependency-updates
        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.get(self, "config"))

    @builtins.property
    @jsii.member(jsii_name="ignoresProjen")
    def ignores_projen(self) -> builtins.bool:
        '''(experimental) Whether or not projen is also upgraded in this config,.

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "ignoresProjen"))


@jsii.data_type(
    jsii_type="projen.github.DependabotIgnore",
    jsii_struct_bases=[],
    name_mapping={"dependency_name": "dependencyName", "versions": "versions"},
)
class DependabotIgnore:
    def __init__(
        self,
        *,
        dependency_name: builtins.str,
        versions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''(experimental) You can use the ``ignore`` option to customize which dependencies are updated.

        The ignore option supports the following options.

        :param dependency_name: (experimental) Use to ignore updates for dependencies with matching names, optionally using ``*`` to match zero or more characters. For Java dependencies, the format of the dependency-name attribute is: ``groupId:artifactId``, for example: ``org.kohsuke:github-api``.
        :param versions: (experimental) Use to ignore specific versions or ranges of versions. If you want to define a range, use the standard pattern for the package manager (for example: ``^1.0.0`` for npm, or ``~> 2.0`` for Bundler).

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e56f402ddf44883464ec12efeaccc97a7e042d533028c01db1fcda57dd3859c8)
            check_type(argname="argument dependency_name", value=dependency_name, expected_type=type_hints["dependency_name"])
            check_type(argname="argument versions", value=versions, expected_type=type_hints["versions"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dependency_name": dependency_name,
        }
        if versions is not None:
            self._values["versions"] = versions

    @builtins.property
    def dependency_name(self) -> builtins.str:
        '''(experimental) Use to ignore updates for dependencies with matching names, optionally using ``*`` to match zero or more characters.

        For Java dependencies, the format of the dependency-name attribute is:
        ``groupId:artifactId``, for example: ``org.kohsuke:github-api``.

        :stability: experimental
        '''
        result = self._values.get("dependency_name")
        assert result is not None, "Required property 'dependency_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def versions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) Use to ignore specific versions or ranges of versions.

        If you want to
        define a range, use the standard pattern for the package manager (for
        example: ``^1.0.0`` for npm, or ``~> 2.0`` for Bundler).

        :stability: experimental
        '''
        result = self._values.get("versions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DependabotIgnore(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.github.DependabotOptions",
    jsii_struct_bases=[],
    name_mapping={
        "ignore": "ignore",
        "ignore_projen": "ignoreProjen",
        "labels": "labels",
        "registries": "registries",
        "schedule_interval": "scheduleInterval",
        "versioning_strategy": "versioningStrategy",
    },
)
class DependabotOptions:
    def __init__(
        self,
        *,
        ignore: typing.Optional[typing.Sequence[typing.Union[DependabotIgnore, typing.Dict[builtins.str, typing.Any]]]] = None,
        ignore_projen: typing.Optional[builtins.bool] = None,
        labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        registries: typing.Optional[typing.Mapping[builtins.str, typing.Union["DependabotRegistry", typing.Dict[builtins.str, typing.Any]]]] = None,
        schedule_interval: typing.Optional["DependabotScheduleInterval"] = None,
        versioning_strategy: typing.Optional["VersioningStrategy"] = None,
    ) -> None:
        '''
        :param ignore: (experimental) You can use the ``ignore`` option to customize which dependencies are updated. The ignore option supports the following options. Default: []
        :param ignore_projen: (experimental) Ignores updates to ``projen``. This is required since projen updates may cause changes in committed files and anti-tamper checks will fail. Projen upgrades are covered through the ``ProjenUpgrade`` class. Default: true
        :param labels: (experimental) List of labels to apply to the created PR's.
        :param registries: (experimental) Map of package registries to use. Default: - use public registries
        :param schedule_interval: (experimental) How often to check for new versions and raise pull requests. Default: ScheduleInterval.DAILY
        :param versioning_strategy: (experimental) The strategy to use when edits manifest and lock files. Default: VersioningStrategy.LOCKFILE_ONLY The default is to only update the lock file because package.json is controlled by projen and any outside updates will fail the build.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0078e67a79ce21c460b876a72b4fbd4a358306502062bdf9bdb13085805a3f2)
            check_type(argname="argument ignore", value=ignore, expected_type=type_hints["ignore"])
            check_type(argname="argument ignore_projen", value=ignore_projen, expected_type=type_hints["ignore_projen"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument registries", value=registries, expected_type=type_hints["registries"])
            check_type(argname="argument schedule_interval", value=schedule_interval, expected_type=type_hints["schedule_interval"])
            check_type(argname="argument versioning_strategy", value=versioning_strategy, expected_type=type_hints["versioning_strategy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ignore is not None:
            self._values["ignore"] = ignore
        if ignore_projen is not None:
            self._values["ignore_projen"] = ignore_projen
        if labels is not None:
            self._values["labels"] = labels
        if registries is not None:
            self._values["registries"] = registries
        if schedule_interval is not None:
            self._values["schedule_interval"] = schedule_interval
        if versioning_strategy is not None:
            self._values["versioning_strategy"] = versioning_strategy

    @builtins.property
    def ignore(self) -> typing.Optional[typing.List[DependabotIgnore]]:
        '''(experimental) You can use the ``ignore`` option to customize which dependencies are updated.

        The ignore option supports the following options.

        :default: []

        :stability: experimental
        '''
        result = self._values.get("ignore")
        return typing.cast(typing.Optional[typing.List[DependabotIgnore]], result)

    @builtins.property
    def ignore_projen(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Ignores updates to ``projen``.

        This is required since projen updates may cause changes in committed files
        and anti-tamper checks will fail.

        Projen upgrades are covered through the ``ProjenUpgrade`` class.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("ignore_projen")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) List of labels to apply to the created PR's.

        :stability: experimental
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def registries(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, "DependabotRegistry"]]:
        '''(experimental) Map of package registries to use.

        :default: - use public registries

        :stability: experimental
        '''
        result = self._values.get("registries")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, "DependabotRegistry"]], result)

    @builtins.property
    def schedule_interval(self) -> typing.Optional["DependabotScheduleInterval"]:
        '''(experimental) How often to check for new versions and raise pull requests.

        :default: ScheduleInterval.DAILY

        :stability: experimental
        '''
        result = self._values.get("schedule_interval")
        return typing.cast(typing.Optional["DependabotScheduleInterval"], result)

    @builtins.property
    def versioning_strategy(self) -> typing.Optional["VersioningStrategy"]:
        '''(experimental) The strategy to use when edits manifest and lock files.

        :default:

        VersioningStrategy.LOCKFILE_ONLY The default is to only update the
        lock file because package.json is controlled by projen and any outside
        updates will fail the build.

        :stability: experimental
        '''
        result = self._values.get("versioning_strategy")
        return typing.cast(typing.Optional["VersioningStrategy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DependabotOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.github.DependabotRegistry",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "url": "url",
        "key": "key",
        "organization": "organization",
        "password": "password",
        "replaces_base": "replacesBase",
        "token": "token",
        "username": "username",
    },
)
class DependabotRegistry:
    def __init__(
        self,
        *,
        type: "DependabotRegistryType",
        url: builtins.str,
        key: typing.Optional[builtins.str] = None,
        organization: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        replaces_base: typing.Optional[builtins.bool] = None,
        token: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Use to add private registry support for dependabot.

        :param type: (experimental) Registry type e.g. 'npm-registry' or 'docker-registry'.
        :param url: (experimental) Url for the registry e.g. 'https://npm.pkg.github.com' or 'registry.hub.docker.com'.
        :param key: (experimental) A reference to a Dependabot secret containing an access key for this registry. Default: undefined
        :param organization: (experimental) Used with the hex-organization registry type. Default: undefined
        :param password: (experimental) A reference to a Dependabot secret containing the password for the specified user. Default: undefined
        :param replaces_base: (experimental) For registries with type: python-index, if the boolean value is true, pip esolves dependencies by using the specified URL rather than the base URL of the Python Package Index (by default https://pypi.org/simple). Default: undefined
        :param token: (experimental) Secret token for dependabot access e.g. '${{ secrets.DEPENDABOT_PACKAGE_TOKEN }}'. Default: undefined
        :param username: (experimental) The username that Dependabot uses to access the registry. Default: - do not authenticate

        :see: https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/configuration-options-for-dependency-updates#configuration-options-for-private-registries
        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71dcef0810bce091e26ea45c125fc125b6b541331dd4f1fa62466d1f52b108d4)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument organization", value=organization, expected_type=type_hints["organization"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument replaces_base", value=replaces_base, expected_type=type_hints["replaces_base"])
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
            "url": url,
        }
        if key is not None:
            self._values["key"] = key
        if organization is not None:
            self._values["organization"] = organization
        if password is not None:
            self._values["password"] = password
        if replaces_base is not None:
            self._values["replaces_base"] = replaces_base
        if token is not None:
            self._values["token"] = token
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def type(self) -> "DependabotRegistryType":
        '''(experimental) Registry type e.g. 'npm-registry' or 'docker-registry'.

        :stability: experimental
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast("DependabotRegistryType", result)

    @builtins.property
    def url(self) -> builtins.str:
        '''(experimental) Url for the registry e.g. 'https://npm.pkg.github.com' or 'registry.hub.docker.com'.

        :stability: experimental
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''(experimental) A reference to a Dependabot secret containing an access key for this registry.

        :default: undefined

        :stability: experimental
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def organization(self) -> typing.Optional[builtins.str]:
        '''(experimental) Used with the hex-organization registry type.

        :default: undefined

        :see: https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/configuration-options-for-dependency-updates#hex-organization
        :stability: experimental
        '''
        result = self._values.get("organization")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''(experimental) A reference to a Dependabot secret containing the password for the specified user.

        :default: undefined

        :stability: experimental
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replaces_base(self) -> typing.Optional[builtins.bool]:
        '''(experimental) For registries with type: python-index, if the boolean value is true, pip esolves dependencies by using the specified URL rather than the base URL of the Python Package Index (by default https://pypi.org/simple).

        :default: undefined

        :stability: experimental
        '''
        result = self._values.get("replaces_base")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def token(self) -> typing.Optional[builtins.str]:
        '''(experimental) Secret token for dependabot access e.g. '${{ secrets.DEPENDABOT_PACKAGE_TOKEN }}'.

        :default: undefined

        :stability: experimental
        '''
        result = self._values.get("token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''(experimental) The username that Dependabot uses to access the registry.

        :default: - do not authenticate

        :stability: experimental
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DependabotRegistry(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="projen.github.DependabotRegistryType")
class DependabotRegistryType(enum.Enum):
    '''(experimental) Each configuration type requires you to provide particular settings.

    Some types allow more than one way to connect

    :see: https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/configuration-options-for-dependency-updates#configuration-options-for-private-registries
    :stability: experimental
    '''

    COMPOSER_REGISTRY = "COMPOSER_REGISTRY"
    '''(experimental) The composer-repository type supports username and password.

    :see: https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/configuration-options-for-dependency-updates#composer-repository
    :stability: experimental
    '''
    DOCKER_REGISTRY = "DOCKER_REGISTRY"
    '''(experimental) The docker-registry type supports username and password.

    The docker-registry type can also be used to pull from Amazon ECR using static AWS credentials

    :see: https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/configuration-options-for-dependency-updates#docker-registry
    :stability: experimental
    '''
    GIT = "GIT"
    '''(experimental) The git type supports username and password.

    :see: https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/configuration-options-for-dependency-updates#git
    :stability: experimental
    '''
    HEX_ORGANIZATION = "HEX_ORGANIZATION"
    '''(experimental) The hex-organization type supports organization and key.

    :see: https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/configuration-options-for-dependency-updates#hex-organization
    :stability: experimental
    '''
    MAVEN_REPOSITORY = "MAVEN_REPOSITORY"
    '''(experimental) The maven-repository type supports username and password, or token.

    :see: https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/configuration-options-for-dependency-updates#maven-repository
    :stability: experimental
    '''
    NPM_REGISTRY = "NPM_REGISTRY"
    '''(experimental) The npm-registry type supports username and password, or token.

    :see: https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/configuration-options-for-dependency-updates#npm-registry
    :stability: experimental
    '''
    NUGET_FEED = "NUGET_FEED"
    '''(experimental) The nuget-feed type supports username and password, or token.

    :see: https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/configuration-options-for-dependency-updates#nuget-feed
    :stability: experimental
    '''
    PYTHON_INDEX = "PYTHON_INDEX"
    '''(experimental) The python-index type supports username and password, or token.

    :see: https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/configuration-options-for-dependency-updates#python-index
    :stability: experimental
    '''
    RUBYGEMS_SERVER = "RUBYGEMS_SERVER"
    '''(experimental) The rubygems-server type supports username and password, or token.

    :see: https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/configuration-options-for-dependency-updates#rubygems-server
    :stability: experimental
    '''
    TERRAFORM_REGISTRY = "TERRAFORM_REGISTRY"
    '''(experimental) The terraform-registry type supports a token.

    :see: https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/configuration-options-for-dependency-updates#terraform-registry
    :stability: experimental
    '''


@jsii.enum(jsii_type="projen.github.DependabotScheduleInterval")
class DependabotScheduleInterval(enum.Enum):
    '''(experimental) How often to check for new versions and raise pull requests for version updates.

    :stability: experimental
    '''

    DAILY = "DAILY"
    '''(experimental) Runs on every weekday, Monday to Friday.

    :stability: experimental
    '''
    WEEKLY = "WEEKLY"
    '''(experimental) Runs once each week.

    By default, this is on Monday.

    :stability: experimental
    '''
    MONTHLY = "MONTHLY"
    '''(experimental) Runs once each month.

    This is on the first day of the month.

    :stability: experimental
    '''


class GitHub(
    _Component_2b0ad27f,
    metaclass=jsii.JSIIMeta,
    jsii_type="projen.github.GitHub",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        project: _Project_57d89203,
        *,
        mergify: typing.Optional[builtins.bool] = None,
        mergify_options: typing.Optional[typing.Union["MergifyOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        projen_credentials: typing.Optional["GithubCredentials"] = None,
        projen_token_secret: typing.Optional[builtins.str] = None,
        pull_request_lint: typing.Optional[builtins.bool] = None,
        pull_request_lint_options: typing.Optional[typing.Union["PullRequestLintOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        workflows: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param project: -
        :param mergify: (experimental) Whether mergify should be enabled on this repository or not. Default: true
        :param mergify_options: (experimental) Options for Mergify. Default: - default options
        :param projen_credentials: (experimental) Choose a method of providing GitHub API access for projen workflows. Default: - use a personal access token named PROJEN_GITHUB_TOKEN
        :param projen_token_secret: (deprecated) The name of a secret which includes a GitHub Personal Access Token to be used by projen workflows. This token needs to have the ``repo``, ``workflows`` and ``packages`` scope. Default: "PROJEN_GITHUB_TOKEN"
        :param pull_request_lint: (experimental) Add a workflow that performs basic checks for pull requests, like validating that PRs follow Conventional Commits. Default: true
        :param pull_request_lint_options: (experimental) Options for configuring a pull request linter. Default: - see defaults in ``PullRequestLintOptions``
        :param workflows: (experimental) Enables GitHub workflows. If this is set to ``false``, workflows will not be created. Default: true

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65db11e8703472c7fa4e013294c649e43b7f8634b29ca11be71b46d8c549c4d1)
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
        options = GitHubOptions(
            mergify=mergify,
            mergify_options=mergify_options,
            projen_credentials=projen_credentials,
            projen_token_secret=projen_token_secret,
            pull_request_lint=pull_request_lint,
            pull_request_lint_options=pull_request_lint_options,
            workflows=workflows,
        )

        jsii.create(self.__class__, self, [project, options])

    @jsii.member(jsii_name="of")
    @builtins.classmethod
    def of(cls, project: _Project_57d89203) -> typing.Optional["GitHub"]:
        '''(experimental) Returns the ``GitHub`` component of a project or ``undefined`` if the project does not have a GitHub component.

        :param project: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1f9f6e10bd4208bf86fd269c2d9b1be37bfe497219300efebf37a151efc972e)
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
        return typing.cast(typing.Optional["GitHub"], jsii.sinvoke(cls, "of", [project]))

    @jsii.member(jsii_name="addDependabot")
    def add_dependabot(
        self,
        *,
        ignore: typing.Optional[typing.Sequence[typing.Union[DependabotIgnore, typing.Dict[builtins.str, typing.Any]]]] = None,
        ignore_projen: typing.Optional[builtins.bool] = None,
        labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        registries: typing.Optional[typing.Mapping[builtins.str, typing.Union[DependabotRegistry, typing.Dict[builtins.str, typing.Any]]]] = None,
        schedule_interval: typing.Optional[DependabotScheduleInterval] = None,
        versioning_strategy: typing.Optional["VersioningStrategy"] = None,
    ) -> Dependabot:
        '''
        :param ignore: (experimental) You can use the ``ignore`` option to customize which dependencies are updated. The ignore option supports the following options. Default: []
        :param ignore_projen: (experimental) Ignores updates to ``projen``. This is required since projen updates may cause changes in committed files and anti-tamper checks will fail. Projen upgrades are covered through the ``ProjenUpgrade`` class. Default: true
        :param labels: (experimental) List of labels to apply to the created PR's.
        :param registries: (experimental) Map of package registries to use. Default: - use public registries
        :param schedule_interval: (experimental) How often to check for new versions and raise pull requests. Default: ScheduleInterval.DAILY
        :param versioning_strategy: (experimental) The strategy to use when edits manifest and lock files. Default: VersioningStrategy.LOCKFILE_ONLY The default is to only update the lock file because package.json is controlled by projen and any outside updates will fail the build.

        :stability: experimental
        '''
        options = DependabotOptions(
            ignore=ignore,
            ignore_projen=ignore_projen,
            labels=labels,
            registries=registries,
            schedule_interval=schedule_interval,
            versioning_strategy=versioning_strategy,
        )

        return typing.cast(Dependabot, jsii.invoke(self, "addDependabot", [options]))

    @jsii.member(jsii_name="addPullRequestTemplate")
    def add_pull_request_template(
        self,
        *content: builtins.str,
    ) -> "PullRequestTemplate":
        '''
        :param content: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4837ecd412981af090d26642873c81c7ca7b69a5c2079c390fb0d3d7168522ff)
            check_type(argname="argument content", value=content, expected_type=typing.Tuple[type_hints["content"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("PullRequestTemplate", jsii.invoke(self, "addPullRequestTemplate", [*content]))

    @jsii.member(jsii_name="addWorkflow")
    def add_workflow(self, name: builtins.str) -> "GithubWorkflow":
        '''(experimental) Adds a workflow to the project.

        :param name: Name of the workflow.

        :return: a GithubWorkflow instance

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79e4dc466f25fa1bf920982b1e4d0a98ce7f5ac928835c4607e7f8879a2e1d06)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        return typing.cast("GithubWorkflow", jsii.invoke(self, "addWorkflow", [name]))

    @jsii.member(jsii_name="tryFindWorkflow")
    def try_find_workflow(
        self,
        name: builtins.str,
    ) -> typing.Optional["GithubWorkflow"]:
        '''(experimental) Finds a GitHub workflow by name.

        Returns ``undefined`` if the workflow cannot be found.

        :param name: The name of the GitHub workflow.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f821cd3bc9db1cb000e2f440c05596f751009b48915d68cabe70e35b8d76b9b)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        return typing.cast(typing.Optional["GithubWorkflow"], jsii.invoke(self, "tryFindWorkflow", [name]))

    @builtins.property
    @jsii.member(jsii_name="actions")
    def actions(self) -> "GitHubActionsProvider":
        '''
        :stability: experimental
        '''
        return typing.cast("GitHubActionsProvider", jsii.get(self, "actions"))

    @builtins.property
    @jsii.member(jsii_name="projenCredentials")
    def projen_credentials(self) -> "GithubCredentials":
        '''(experimental) GitHub API authentication method used by projen workflows.

        :stability: experimental
        '''
        return typing.cast("GithubCredentials", jsii.get(self, "projenCredentials"))

    @builtins.property
    @jsii.member(jsii_name="workflows")
    def workflows(self) -> typing.List["GithubWorkflow"]:
        '''(experimental) All workflows.

        :stability: experimental
        '''
        return typing.cast(typing.List["GithubWorkflow"], jsii.get(self, "workflows"))

    @builtins.property
    @jsii.member(jsii_name="workflowsEnabled")
    def workflows_enabled(self) -> builtins.bool:
        '''(experimental) Are workflows enabled?

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "workflowsEnabled"))

    @builtins.property
    @jsii.member(jsii_name="mergify")
    def mergify(self) -> typing.Optional["Mergify"]:
        '''(experimental) The ``Mergify`` configured on this repository.

        This is ``undefined`` if Mergify
        was not enabled when creating the repository.

        :stability: experimental
        '''
        return typing.cast(typing.Optional["Mergify"], jsii.get(self, "mergify"))


class GitHubActionsProvider(
    metaclass=jsii.JSIIMeta,
    jsii_type="projen.github.GitHubActionsProvider",
):
    '''(experimental) Manage the versions used for GitHub Actions used in steps.

    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="get")
    def get(self, action: builtins.str) -> builtins.str:
        '''(experimental) Resolve an action name to the version that should be used, taking into account any overrides.

        :param action: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24cff0cda4c3df59446abb56b6381699178c88cc41a2184a819684d64a6d343c)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
        return typing.cast(builtins.str, jsii.invoke(self, "get", [action]))

    @jsii.member(jsii_name="set")
    def set(self, action: builtins.str, override: builtins.str) -> None:
        '''(experimental) Define an override for a given action.

        Specify the action name without a version to override all usages of the action.
        You can also override a specific action version, by providing the version string.
        Specific overrides take precedence over overrides without a version.

        If an override for the same action name is set multiple times, the last override is used.

        :param action: -
        :param override: -

        :stability: experimental

        Example::

            // Force any use of `actions/checkout` to use a pin a specific commit
            project.github.actions.set("actions/checkout", "actions/checkout@aaaaaa");
            
            // But pin usage of `v3` to a different commit
            project.github.actions.set("actions/checkout@v3", "actions/checkout@ffffff");
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20166ac47381861e1a45b550a5e9646380c52a927fca9ebf00ec36dab0f295ed)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument override", value=override, expected_type=type_hints["override"])
        return typing.cast(None, jsii.invoke(self, "set", [action, override]))


@jsii.data_type(
    jsii_type="projen.github.GitHubOptions",
    jsii_struct_bases=[],
    name_mapping={
        "mergify": "mergify",
        "mergify_options": "mergifyOptions",
        "projen_credentials": "projenCredentials",
        "projen_token_secret": "projenTokenSecret",
        "pull_request_lint": "pullRequestLint",
        "pull_request_lint_options": "pullRequestLintOptions",
        "workflows": "workflows",
    },
)
class GitHubOptions:
    def __init__(
        self,
        *,
        mergify: typing.Optional[builtins.bool] = None,
        mergify_options: typing.Optional[typing.Union["MergifyOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        projen_credentials: typing.Optional["GithubCredentials"] = None,
        projen_token_secret: typing.Optional[builtins.str] = None,
        pull_request_lint: typing.Optional[builtins.bool] = None,
        pull_request_lint_options: typing.Optional[typing.Union["PullRequestLintOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        workflows: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param mergify: (experimental) Whether mergify should be enabled on this repository or not. Default: true
        :param mergify_options: (experimental) Options for Mergify. Default: - default options
        :param projen_credentials: (experimental) Choose a method of providing GitHub API access for projen workflows. Default: - use a personal access token named PROJEN_GITHUB_TOKEN
        :param projen_token_secret: (deprecated) The name of a secret which includes a GitHub Personal Access Token to be used by projen workflows. This token needs to have the ``repo``, ``workflows`` and ``packages`` scope. Default: "PROJEN_GITHUB_TOKEN"
        :param pull_request_lint: (experimental) Add a workflow that performs basic checks for pull requests, like validating that PRs follow Conventional Commits. Default: true
        :param pull_request_lint_options: (experimental) Options for configuring a pull request linter. Default: - see defaults in ``PullRequestLintOptions``
        :param workflows: (experimental) Enables GitHub workflows. If this is set to ``false``, workflows will not be created. Default: true

        :stability: experimental
        '''
        if isinstance(mergify_options, dict):
            mergify_options = MergifyOptions(**mergify_options)
        if isinstance(pull_request_lint_options, dict):
            pull_request_lint_options = PullRequestLintOptions(**pull_request_lint_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c22e66f011c96f13a6f4e5b07bb676bf98b477678e968ee61f79ee107a7d2bd7)
            check_type(argname="argument mergify", value=mergify, expected_type=type_hints["mergify"])
            check_type(argname="argument mergify_options", value=mergify_options, expected_type=type_hints["mergify_options"])
            check_type(argname="argument projen_credentials", value=projen_credentials, expected_type=type_hints["projen_credentials"])
            check_type(argname="argument projen_token_secret", value=projen_token_secret, expected_type=type_hints["projen_token_secret"])
            check_type(argname="argument pull_request_lint", value=pull_request_lint, expected_type=type_hints["pull_request_lint"])
            check_type(argname="argument pull_request_lint_options", value=pull_request_lint_options, expected_type=type_hints["pull_request_lint_options"])
            check_type(argname="argument workflows", value=workflows, expected_type=type_hints["workflows"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if mergify is not None:
            self._values["mergify"] = mergify
        if mergify_options is not None:
            self._values["mergify_options"] = mergify_options
        if projen_credentials is not None:
            self._values["projen_credentials"] = projen_credentials
        if projen_token_secret is not None:
            self._values["projen_token_secret"] = projen_token_secret
        if pull_request_lint is not None:
            self._values["pull_request_lint"] = pull_request_lint
        if pull_request_lint_options is not None:
            self._values["pull_request_lint_options"] = pull_request_lint_options
        if workflows is not None:
            self._values["workflows"] = workflows

    @builtins.property
    def mergify(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether mergify should be enabled on this repository or not.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("mergify")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def mergify_options(self) -> typing.Optional["MergifyOptions"]:
        '''(experimental) Options for Mergify.

        :default: - default options

        :stability: experimental
        '''
        result = self._values.get("mergify_options")
        return typing.cast(typing.Optional["MergifyOptions"], result)

    @builtins.property
    def projen_credentials(self) -> typing.Optional["GithubCredentials"]:
        '''(experimental) Choose a method of providing GitHub API access for projen workflows.

        :default: - use a personal access token named PROJEN_GITHUB_TOKEN

        :stability: experimental
        '''
        result = self._values.get("projen_credentials")
        return typing.cast(typing.Optional["GithubCredentials"], result)

    @builtins.property
    def projen_token_secret(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The name of a secret which includes a GitHub Personal Access Token to be used by projen workflows.

        This token needs to have the ``repo``, ``workflows``
        and ``packages`` scope.

        :default: "PROJEN_GITHUB_TOKEN"

        :deprecated: - use ``projenCredentials``

        :stability: deprecated
        '''
        result = self._values.get("projen_token_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pull_request_lint(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Add a workflow that performs basic checks for pull requests, like validating that PRs follow Conventional Commits.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("pull_request_lint")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def pull_request_lint_options(self) -> typing.Optional["PullRequestLintOptions"]:
        '''(experimental) Options for configuring a pull request linter.

        :default: - see defaults in ``PullRequestLintOptions``

        :stability: experimental
        '''
        result = self._values.get("pull_request_lint_options")
        return typing.cast(typing.Optional["PullRequestLintOptions"], result)

    @builtins.property
    def workflows(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Enables GitHub workflows.

        If this is set to ``false``, workflows will not be created.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("workflows")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GitHubOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GitHubProject(
    _Project_57d89203,
    metaclass=jsii.JSIIMeta,
    jsii_type="projen.github.GitHubProject",
):
    '''(deprecated) GitHub-based project.

    :deprecated:

    This is a *temporary* class. At the moment, our base project
    types such as ``NodeProject`` and ``JavaProject`` are derived from this, but we
    want to be able to use these project types outside of GitHub as well. One of
    the next steps to address this is to abstract workflows so that different
    "engines" can be used to implement our CI/CD solutions.

    :stability: deprecated
    '''

    def __init__(
        self,
        *,
        auto_approve_options: typing.Optional[typing.Union[AutoApproveOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        auto_merge: typing.Optional[builtins.bool] = None,
        auto_merge_options: typing.Optional[typing.Union[AutoMergeOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        clobber: typing.Optional[builtins.bool] = None,
        dev_container: typing.Optional[builtins.bool] = None,
        github: typing.Optional[builtins.bool] = None,
        github_options: typing.Optional[typing.Union[GitHubOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        gitpod: typing.Optional[builtins.bool] = None,
        mergify: typing.Optional[builtins.bool] = None,
        mergify_options: typing.Optional[typing.Union["MergifyOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        project_type: typing.Optional[_ProjectType_fd80c725] = None,
        projen_credentials: typing.Optional["GithubCredentials"] = None,
        projen_token_secret: typing.Optional[builtins.str] = None,
        readme: typing.Optional[typing.Union[_SampleReadmeProps_3518b03b, typing.Dict[builtins.str, typing.Any]]] = None,
        stale: typing.Optional[builtins.bool] = None,
        stale_options: typing.Optional[typing.Union["StaleOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        vscode: typing.Optional[builtins.bool] = None,
        name: builtins.str,
        commit_generated: typing.Optional[builtins.bool] = None,
        logging: typing.Optional[typing.Union[_LoggerOptions_eb0f6309, typing.Dict[builtins.str, typing.Any]]] = None,
        outdir: typing.Optional[builtins.str] = None,
        parent: typing.Optional[_Project_57d89203] = None,
        projen_command: typing.Optional[builtins.str] = None,
        projenrc_json: typing.Optional[builtins.bool] = None,
        projenrc_json_options: typing.Optional[typing.Union[_ProjenrcOptions_164bd039, typing.Dict[builtins.str, typing.Any]]] = None,
        renovatebot: typing.Optional[builtins.bool] = None,
        renovatebot_options: typing.Optional[typing.Union[_RenovatebotOptions_18e6b8a1, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param auto_approve_options: (experimental) Enable and configure the 'auto approve' workflow. Default: - auto approve is disabled
        :param auto_merge: (experimental) Enable automatic merging on GitHub. Has no effect if ``github.mergify`` is set to false. Default: true
        :param auto_merge_options: (experimental) Configure options for automatic merging on GitHub. Has no effect if ``github.mergify`` or ``autoMerge`` is set to false. Default: - see defaults in ``AutoMergeOptions``
        :param clobber: (experimental) Add a ``clobber`` task which resets the repo to origin. Default: true
        :param dev_container: (experimental) Add a VSCode development environment (used for GitHub Codespaces). Default: false
        :param github: (experimental) Enable GitHub integration. Enabled by default for root projects. Disabled for non-root projects. Default: true
        :param github_options: (experimental) Options for GitHub integration. Default: - see GitHubOptions
        :param gitpod: (experimental) Add a Gitpod development environment. Default: false
        :param mergify: (deprecated) Whether mergify should be enabled on this repository or not. Default: true
        :param mergify_options: (deprecated) Options for mergify. Default: - default options
        :param project_type: (deprecated) Which type of project this is (library/app). Default: ProjectType.UNKNOWN
        :param projen_credentials: (experimental) Choose a method of providing GitHub API access for projen workflows. Default: - use a personal access token named PROJEN_GITHUB_TOKEN
        :param projen_token_secret: (deprecated) The name of a secret which includes a GitHub Personal Access Token to be used by projen workflows. This token needs to have the ``repo``, ``workflows`` and ``packages`` scope. Default: "PROJEN_GITHUB_TOKEN"
        :param readme: (experimental) The README setup. Default: - { filename: 'README.md', contents: '# replace this' }
        :param stale: (experimental) Auto-close of stale issues and pull request. See ``staleOptions`` for options. Default: false
        :param stale_options: (experimental) Auto-close stale issues and pull requests. To disable set ``stale`` to ``false``. Default: - see defaults in ``StaleOptions``
        :param vscode: (experimental) Enable VSCode integration. Enabled by default for root projects. Disabled for non-root projects. Default: true
        :param name: (experimental) This is the name of your project. Default: $BASEDIR
        :param commit_generated: (experimental) Whether to commit the managed files by default. Default: true
        :param logging: (experimental) Configure logging options such as verbosity. Default: {}
        :param outdir: (experimental) The root directory of the project. Relative to this directory, all files are synthesized. If this project has a parent, this directory is relative to the parent directory and it cannot be the same as the parent or any of it's other sub-projects. Default: "."
        :param parent: (experimental) The parent project, if this project is part of a bigger project.
        :param projen_command: (experimental) The shell command to use in order to run the projen CLI. Can be used to customize in special environments. Default: "npx projen"
        :param projenrc_json: (experimental) Generate (once) .projenrc.json (in JSON). Set to ``false`` in order to disable .projenrc.json generation. Default: false
        :param projenrc_json_options: (experimental) Options for .projenrc.json. Default: - default options
        :param renovatebot: (experimental) Use renovatebot to handle dependency upgrades. Default: false
        :param renovatebot_options: (experimental) Options for renovatebot. Default: - default options

        :stability: deprecated
        '''
        options = GitHubProjectOptions(
            auto_approve_options=auto_approve_options,
            auto_merge=auto_merge,
            auto_merge_options=auto_merge_options,
            clobber=clobber,
            dev_container=dev_container,
            github=github,
            github_options=github_options,
            gitpod=gitpod,
            mergify=mergify,
            mergify_options=mergify_options,
            project_type=project_type,
            projen_credentials=projen_credentials,
            projen_token_secret=projen_token_secret,
            readme=readme,
            stale=stale,
            stale_options=stale_options,
            vscode=vscode,
            name=name,
            commit_generated=commit_generated,
            logging=logging,
            outdir=outdir,
            parent=parent,
            projen_command=projen_command,
            projenrc_json=projenrc_json,
            projenrc_json_options=projenrc_json_options,
            renovatebot=renovatebot,
            renovatebot_options=renovatebot_options,
        )

        jsii.create(self.__class__, self, [options])

    @jsii.member(jsii_name="annotateGenerated")
    def annotate_generated(self, glob: builtins.str) -> None:
        '''(deprecated) Marks the provided file(s) as being generated.

        This is achieved using the
        github-linguist attributes. Generated files do not count against the
        repository statistics and language breakdown.

        :param glob: the glob pattern to match (could be a file path).

        :see: https://github.com/github/linguist/blob/master/docs/overrides.md
        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d5a31d0302f973c0cd7ab51b14219e96872615cf2769150b28c23b8bb3a09fc)
            check_type(argname="argument glob", value=glob, expected_type=type_hints["glob"])
        return typing.cast(None, jsii.invoke(self, "annotateGenerated", [glob]))

    @builtins.property
    @jsii.member(jsii_name="projectType")
    def project_type(self) -> _ProjectType_fd80c725:
        '''
        :stability: deprecated
        '''
        return typing.cast(_ProjectType_fd80c725, jsii.get(self, "projectType"))

    @builtins.property
    @jsii.member(jsii_name="autoApprove")
    def auto_approve(self) -> typing.Optional[AutoApprove]:
        '''(deprecated) Auto approve set up for this project.

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[AutoApprove], jsii.get(self, "autoApprove"))

    @builtins.property
    @jsii.member(jsii_name="devContainer")
    def dev_container(self) -> typing.Optional[_DevContainer_ae6f3538]:
        '''(deprecated) Access for .devcontainer.json (used for GitHub Codespaces).

        This will be ``undefined`` if devContainer boolean is false

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[_DevContainer_ae6f3538], jsii.get(self, "devContainer"))

    @builtins.property
    @jsii.member(jsii_name="github")
    def github(self) -> typing.Optional[GitHub]:
        '''(deprecated) Access all github components.

        This will be ``undefined`` for subprojects.

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[GitHub], jsii.get(self, "github"))

    @builtins.property
    @jsii.member(jsii_name="gitpod")
    def gitpod(self) -> typing.Optional[_Gitpod_5d9b9d87]:
        '''(deprecated) Access for Gitpod.

        This will be ``undefined`` if gitpod boolean is false

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[_Gitpod_5d9b9d87], jsii.get(self, "gitpod"))

    @builtins.property
    @jsii.member(jsii_name="vscode")
    def vscode(self) -> typing.Optional[_VsCode_9f0f4eb5]:
        '''(deprecated) Access all VSCode components.

        This will be ``undefined`` for subprojects.

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[_VsCode_9f0f4eb5], jsii.get(self, "vscode"))


@jsii.data_type(
    jsii_type="projen.github.GitHubProjectOptions",
    jsii_struct_bases=[_ProjectOptions_0d5b93c6],
    name_mapping={
        "name": "name",
        "commit_generated": "commitGenerated",
        "logging": "logging",
        "outdir": "outdir",
        "parent": "parent",
        "projen_command": "projenCommand",
        "projenrc_json": "projenrcJson",
        "projenrc_json_options": "projenrcJsonOptions",
        "renovatebot": "renovatebot",
        "renovatebot_options": "renovatebotOptions",
        "auto_approve_options": "autoApproveOptions",
        "auto_merge": "autoMerge",
        "auto_merge_options": "autoMergeOptions",
        "clobber": "clobber",
        "dev_container": "devContainer",
        "github": "github",
        "github_options": "githubOptions",
        "gitpod": "gitpod",
        "mergify": "mergify",
        "mergify_options": "mergifyOptions",
        "project_type": "projectType",
        "projen_credentials": "projenCredentials",
        "projen_token_secret": "projenTokenSecret",
        "readme": "readme",
        "stale": "stale",
        "stale_options": "staleOptions",
        "vscode": "vscode",
    },
)
class GitHubProjectOptions(_ProjectOptions_0d5b93c6):
    def __init__(
        self,
        *,
        name: builtins.str,
        commit_generated: typing.Optional[builtins.bool] = None,
        logging: typing.Optional[typing.Union[_LoggerOptions_eb0f6309, typing.Dict[builtins.str, typing.Any]]] = None,
        outdir: typing.Optional[builtins.str] = None,
        parent: typing.Optional[_Project_57d89203] = None,
        projen_command: typing.Optional[builtins.str] = None,
        projenrc_json: typing.Optional[builtins.bool] = None,
        projenrc_json_options: typing.Optional[typing.Union[_ProjenrcOptions_164bd039, typing.Dict[builtins.str, typing.Any]]] = None,
        renovatebot: typing.Optional[builtins.bool] = None,
        renovatebot_options: typing.Optional[typing.Union[_RenovatebotOptions_18e6b8a1, typing.Dict[builtins.str, typing.Any]]] = None,
        auto_approve_options: typing.Optional[typing.Union[AutoApproveOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        auto_merge: typing.Optional[builtins.bool] = None,
        auto_merge_options: typing.Optional[typing.Union[AutoMergeOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        clobber: typing.Optional[builtins.bool] = None,
        dev_container: typing.Optional[builtins.bool] = None,
        github: typing.Optional[builtins.bool] = None,
        github_options: typing.Optional[typing.Union[GitHubOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        gitpod: typing.Optional[builtins.bool] = None,
        mergify: typing.Optional[builtins.bool] = None,
        mergify_options: typing.Optional[typing.Union["MergifyOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        project_type: typing.Optional[_ProjectType_fd80c725] = None,
        projen_credentials: typing.Optional["GithubCredentials"] = None,
        projen_token_secret: typing.Optional[builtins.str] = None,
        readme: typing.Optional[typing.Union[_SampleReadmeProps_3518b03b, typing.Dict[builtins.str, typing.Any]]] = None,
        stale: typing.Optional[builtins.bool] = None,
        stale_options: typing.Optional[typing.Union["StaleOptions", typing.Dict[builtins.str, typing.Any]]] = None,
        vscode: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Options for ``GitHubProject``.

        :param name: (experimental) This is the name of your project. Default: $BASEDIR
        :param commit_generated: (experimental) Whether to commit the managed files by default. Default: true
        :param logging: (experimental) Configure logging options such as verbosity. Default: {}
        :param outdir: (experimental) The root directory of the project. Relative to this directory, all files are synthesized. If this project has a parent, this directory is relative to the parent directory and it cannot be the same as the parent or any of it's other sub-projects. Default: "."
        :param parent: (experimental) The parent project, if this project is part of a bigger project.
        :param projen_command: (experimental) The shell command to use in order to run the projen CLI. Can be used to customize in special environments. Default: "npx projen"
        :param projenrc_json: (experimental) Generate (once) .projenrc.json (in JSON). Set to ``false`` in order to disable .projenrc.json generation. Default: false
        :param projenrc_json_options: (experimental) Options for .projenrc.json. Default: - default options
        :param renovatebot: (experimental) Use renovatebot to handle dependency upgrades. Default: false
        :param renovatebot_options: (experimental) Options for renovatebot. Default: - default options
        :param auto_approve_options: (experimental) Enable and configure the 'auto approve' workflow. Default: - auto approve is disabled
        :param auto_merge: (experimental) Enable automatic merging on GitHub. Has no effect if ``github.mergify`` is set to false. Default: true
        :param auto_merge_options: (experimental) Configure options for automatic merging on GitHub. Has no effect if ``github.mergify`` or ``autoMerge`` is set to false. Default: - see defaults in ``AutoMergeOptions``
        :param clobber: (experimental) Add a ``clobber`` task which resets the repo to origin. Default: true
        :param dev_container: (experimental) Add a VSCode development environment (used for GitHub Codespaces). Default: false
        :param github: (experimental) Enable GitHub integration. Enabled by default for root projects. Disabled for non-root projects. Default: true
        :param github_options: (experimental) Options for GitHub integration. Default: - see GitHubOptions
        :param gitpod: (experimental) Add a Gitpod development environment. Default: false
        :param mergify: (deprecated) Whether mergify should be enabled on this repository or not. Default: true
        :param mergify_options: (deprecated) Options for mergify. Default: - default options
        :param project_type: (deprecated) Which type of project this is (library/app). Default: ProjectType.UNKNOWN
        :param projen_credentials: (experimental) Choose a method of providing GitHub API access for projen workflows. Default: - use a personal access token named PROJEN_GITHUB_TOKEN
        :param projen_token_secret: (deprecated) The name of a secret which includes a GitHub Personal Access Token to be used by projen workflows. This token needs to have the ``repo``, ``workflows`` and ``packages`` scope. Default: "PROJEN_GITHUB_TOKEN"
        :param readme: (experimental) The README setup. Default: - { filename: 'README.md', contents: '# replace this' }
        :param stale: (experimental) Auto-close of stale issues and pull request. See ``staleOptions`` for options. Default: false
        :param stale_options: (experimental) Auto-close stale issues and pull requests. To disable set ``stale`` to ``false``. Default: - see defaults in ``StaleOptions``
        :param vscode: (experimental) Enable VSCode integration. Enabled by default for root projects. Disabled for non-root projects. Default: true

        :stability: experimental
        '''
        if isinstance(logging, dict):
            logging = _LoggerOptions_eb0f6309(**logging)
        if isinstance(projenrc_json_options, dict):
            projenrc_json_options = _ProjenrcOptions_164bd039(**projenrc_json_options)
        if isinstance(renovatebot_options, dict):
            renovatebot_options = _RenovatebotOptions_18e6b8a1(**renovatebot_options)
        if isinstance(auto_approve_options, dict):
            auto_approve_options = AutoApproveOptions(**auto_approve_options)
        if isinstance(auto_merge_options, dict):
            auto_merge_options = AutoMergeOptions(**auto_merge_options)
        if isinstance(github_options, dict):
            github_options = GitHubOptions(**github_options)
        if isinstance(mergify_options, dict):
            mergify_options = MergifyOptions(**mergify_options)
        if isinstance(readme, dict):
            readme = _SampleReadmeProps_3518b03b(**readme)
        if isinstance(stale_options, dict):
            stale_options = StaleOptions(**stale_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e987504475149e2e7d9b25ee3320e9bdd8afa45a0da64af7b3a153489524cd70)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument commit_generated", value=commit_generated, expected_type=type_hints["commit_generated"])
            check_type(argname="argument logging", value=logging, expected_type=type_hints["logging"])
            check_type(argname="argument outdir", value=outdir, expected_type=type_hints["outdir"])
            check_type(argname="argument parent", value=parent, expected_type=type_hints["parent"])
            check_type(argname="argument projen_command", value=projen_command, expected_type=type_hints["projen_command"])
            check_type(argname="argument projenrc_json", value=projenrc_json, expected_type=type_hints["projenrc_json"])
            check_type(argname="argument projenrc_json_options", value=projenrc_json_options, expected_type=type_hints["projenrc_json_options"])
            check_type(argname="argument renovatebot", value=renovatebot, expected_type=type_hints["renovatebot"])
            check_type(argname="argument renovatebot_options", value=renovatebot_options, expected_type=type_hints["renovatebot_options"])
            check_type(argname="argument auto_approve_options", value=auto_approve_options, expected_type=type_hints["auto_approve_options"])
            check_type(argname="argument auto_merge", value=auto_merge, expected_type=type_hints["auto_merge"])
            check_type(argname="argument auto_merge_options", value=auto_merge_options, expected_type=type_hints["auto_merge_options"])
            check_type(argname="argument clobber", value=clobber, expected_type=type_hints["clobber"])
            check_type(argname="argument dev_container", value=dev_container, expected_type=type_hints["dev_container"])
            check_type(argname="argument github", value=github, expected_type=type_hints["github"])
            check_type(argname="argument github_options", value=github_options, expected_type=type_hints["github_options"])
            check_type(argname="argument gitpod", value=gitpod, expected_type=type_hints["gitpod"])
            check_type(argname="argument mergify", value=mergify, expected_type=type_hints["mergify"])
            check_type(argname="argument mergify_options", value=mergify_options, expected_type=type_hints["mergify_options"])
            check_type(argname="argument project_type", value=project_type, expected_type=type_hints["project_type"])
            check_type(argname="argument projen_credentials", value=projen_credentials, expected_type=type_hints["projen_credentials"])
            check_type(argname="argument projen_token_secret", value=projen_token_secret, expected_type=type_hints["projen_token_secret"])
            check_type(argname="argument readme", value=readme, expected_type=type_hints["readme"])
            check_type(argname="argument stale", value=stale, expected_type=type_hints["stale"])
            check_type(argname="argument stale_options", value=stale_options, expected_type=type_hints["stale_options"])
            check_type(argname="argument vscode", value=vscode, expected_type=type_hints["vscode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if commit_generated is not None:
            self._values["commit_generated"] = commit_generated
        if logging is not None:
            self._values["logging"] = logging
        if outdir is not None:
            self._values["outdir"] = outdir
        if parent is not None:
            self._values["parent"] = parent
        if projen_command is not None:
            self._values["projen_command"] = projen_command
        if projenrc_json is not None:
            self._values["projenrc_json"] = projenrc_json
        if projenrc_json_options is not None:
            self._values["projenrc_json_options"] = projenrc_json_options
        if renovatebot is not None:
            self._values["renovatebot"] = renovatebot
        if renovatebot_options is not None:
            self._values["renovatebot_options"] = renovatebot_options
        if auto_approve_options is not None:
            self._values["auto_approve_options"] = auto_approve_options
        if auto_merge is not None:
            self._values["auto_merge"] = auto_merge
        if auto_merge_options is not None:
            self._values["auto_merge_options"] = auto_merge_options
        if clobber is not None:
            self._values["clobber"] = clobber
        if dev_container is not None:
            self._values["dev_container"] = dev_container
        if github is not None:
            self._values["github"] = github
        if github_options is not None:
            self._values["github_options"] = github_options
        if gitpod is not None:
            self._values["gitpod"] = gitpod
        if mergify is not None:
            self._values["mergify"] = mergify
        if mergify_options is not None:
            self._values["mergify_options"] = mergify_options
        if project_type is not None:
            self._values["project_type"] = project_type
        if projen_credentials is not None:
            self._values["projen_credentials"] = projen_credentials
        if projen_token_secret is not None:
            self._values["projen_token_secret"] = projen_token_secret
        if readme is not None:
            self._values["readme"] = readme
        if stale is not None:
            self._values["stale"] = stale
        if stale_options is not None:
            self._values["stale_options"] = stale_options
        if vscode is not None:
            self._values["vscode"] = vscode

    @builtins.property
    def name(self) -> builtins.str:
        '''(experimental) This is the name of your project.

        :default: $BASEDIR

        :stability: experimental
        :featured: true
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def commit_generated(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether to commit the managed files by default.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("commit_generated")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def logging(self) -> typing.Optional[_LoggerOptions_eb0f6309]:
        '''(experimental) Configure logging options such as verbosity.

        :default: {}

        :stability: experimental
        '''
        result = self._values.get("logging")
        return typing.cast(typing.Optional[_LoggerOptions_eb0f6309], result)

    @builtins.property
    def outdir(self) -> typing.Optional[builtins.str]:
        '''(experimental) The root directory of the project.

        Relative to this directory, all files are synthesized.

        If this project has a parent, this directory is relative to the parent
        directory and it cannot be the same as the parent or any of it's other
        sub-projects.

        :default: "."

        :stability: experimental
        '''
        result = self._values.get("outdir")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parent(self) -> typing.Optional[_Project_57d89203]:
        '''(experimental) The parent project, if this project is part of a bigger project.

        :stability: experimental
        '''
        result = self._values.get("parent")
        return typing.cast(typing.Optional[_Project_57d89203], result)

    @builtins.property
    def projen_command(self) -> typing.Optional[builtins.str]:
        '''(experimental) The shell command to use in order to run the projen CLI.

        Can be used to customize in special environments.

        :default: "npx projen"

        :stability: experimental
        '''
        result = self._values.get("projen_command")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def projenrc_json(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Generate (once) .projenrc.json (in JSON). Set to ``false`` in order to disable .projenrc.json generation.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("projenrc_json")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def projenrc_json_options(self) -> typing.Optional[_ProjenrcOptions_164bd039]:
        '''(experimental) Options for .projenrc.json.

        :default: - default options

        :stability: experimental
        '''
        result = self._values.get("projenrc_json_options")
        return typing.cast(typing.Optional[_ProjenrcOptions_164bd039], result)

    @builtins.property
    def renovatebot(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Use renovatebot to handle dependency upgrades.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("renovatebot")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def renovatebot_options(self) -> typing.Optional[_RenovatebotOptions_18e6b8a1]:
        '''(experimental) Options for renovatebot.

        :default: - default options

        :stability: experimental
        '''
        result = self._values.get("renovatebot_options")
        return typing.cast(typing.Optional[_RenovatebotOptions_18e6b8a1], result)

    @builtins.property
    def auto_approve_options(self) -> typing.Optional[AutoApproveOptions]:
        '''(experimental) Enable and configure the 'auto approve' workflow.

        :default: - auto approve is disabled

        :stability: experimental
        '''
        result = self._values.get("auto_approve_options")
        return typing.cast(typing.Optional[AutoApproveOptions], result)

    @builtins.property
    def auto_merge(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Enable automatic merging on GitHub.

        Has no effect if ``github.mergify``
        is set to false.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("auto_merge")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def auto_merge_options(self) -> typing.Optional[AutoMergeOptions]:
        '''(experimental) Configure options for automatic merging on GitHub.

        Has no effect if
        ``github.mergify`` or ``autoMerge`` is set to false.

        :default: - see defaults in ``AutoMergeOptions``

        :stability: experimental
        '''
        result = self._values.get("auto_merge_options")
        return typing.cast(typing.Optional[AutoMergeOptions], result)

    @builtins.property
    def clobber(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Add a ``clobber`` task which resets the repo to origin.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("clobber")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def dev_container(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Add a VSCode development environment (used for GitHub Codespaces).

        :default: false

        :stability: experimental
        '''
        result = self._values.get("dev_container")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def github(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Enable GitHub integration.

        Enabled by default for root projects. Disabled for non-root projects.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("github")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def github_options(self) -> typing.Optional[GitHubOptions]:
        '''(experimental) Options for GitHub integration.

        :default: - see GitHubOptions

        :stability: experimental
        '''
        result = self._values.get("github_options")
        return typing.cast(typing.Optional[GitHubOptions], result)

    @builtins.property
    def gitpod(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Add a Gitpod development environment.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("gitpod")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def mergify(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Whether mergify should be enabled on this repository or not.

        :default: true

        :deprecated: use ``githubOptions.mergify`` instead

        :stability: deprecated
        '''
        result = self._values.get("mergify")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def mergify_options(self) -> typing.Optional["MergifyOptions"]:
        '''(deprecated) Options for mergify.

        :default: - default options

        :deprecated: use ``githubOptions.mergifyOptions`` instead

        :stability: deprecated
        '''
        result = self._values.get("mergify_options")
        return typing.cast(typing.Optional["MergifyOptions"], result)

    @builtins.property
    def project_type(self) -> typing.Optional[_ProjectType_fd80c725]:
        '''(deprecated) Which type of project this is (library/app).

        :default: ProjectType.UNKNOWN

        :deprecated: no longer supported at the base project level

        :stability: deprecated
        '''
        result = self._values.get("project_type")
        return typing.cast(typing.Optional[_ProjectType_fd80c725], result)

    @builtins.property
    def projen_credentials(self) -> typing.Optional["GithubCredentials"]:
        '''(experimental) Choose a method of providing GitHub API access for projen workflows.

        :default: - use a personal access token named PROJEN_GITHUB_TOKEN

        :stability: experimental
        '''
        result = self._values.get("projen_credentials")
        return typing.cast(typing.Optional["GithubCredentials"], result)

    @builtins.property
    def projen_token_secret(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The name of a secret which includes a GitHub Personal Access Token to be used by projen workflows.

        This token needs to have the ``repo``, ``workflows``
        and ``packages`` scope.

        :default: "PROJEN_GITHUB_TOKEN"

        :deprecated: use ``projenCredentials``

        :stability: deprecated
        '''
        result = self._values.get("projen_token_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def readme(self) -> typing.Optional[_SampleReadmeProps_3518b03b]:
        '''(experimental) The README setup.

        :default: - { filename: 'README.md', contents: '# replace this' }

        :stability: experimental

        Example::

            "{ filename: 'readme.md', contents: '# title' }"
        '''
        result = self._values.get("readme")
        return typing.cast(typing.Optional[_SampleReadmeProps_3518b03b], result)

    @builtins.property
    def stale(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Auto-close of stale issues and pull request.

        See ``staleOptions`` for options.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("stale")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def stale_options(self) -> typing.Optional["StaleOptions"]:
        '''(experimental) Auto-close stale issues and pull requests.

        To disable set ``stale`` to ``false``.

        :default: - see defaults in ``StaleOptions``

        :stability: experimental
        '''
        result = self._values.get("stale_options")
        return typing.cast(typing.Optional["StaleOptions"], result)

    @builtins.property
    def vscode(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Enable VSCode integration.

        Enabled by default for root projects. Disabled for non-root projects.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("vscode")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GitHubProjectOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.github.GitIdentity",
    jsii_struct_bases=[],
    name_mapping={"email": "email", "name": "name"},
)
class GitIdentity:
    def __init__(self, *, email: builtins.str, name: builtins.str) -> None:
        '''(experimental) Represents the git identity.

        :param email: (experimental) The email address of the git user.
        :param name: (experimental) The name of the user.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9975d58a3cca9992aa51d0da1572c207d374c146dec0474fc911a56739c487e)
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "email": email,
            "name": name,
        }

    @builtins.property
    def email(self) -> builtins.str:
        '''(experimental) The email address of the git user.

        :stability: experimental
        '''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''(experimental) The name of the user.

        :stability: experimental
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GitIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GithubCredentials(
    metaclass=jsii.JSIIMeta,
    jsii_type="projen.github.GithubCredentials",
):
    '''(experimental) Represents a method of providing GitHub API access for projen workflows.

    :stability: experimental
    '''

    @jsii.member(jsii_name="fromApp")
    @builtins.classmethod
    def from_app(
        cls,
        *,
        app_id_secret: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[typing.Union[_AppPermissions_59709d51, typing.Dict[builtins.str, typing.Any]]] = None,
        private_key_secret: typing.Optional[builtins.str] = None,
    ) -> "GithubCredentials":
        '''(experimental) Provide API access through a GitHub App.

        The GitHub App must be installed on the GitHub repo, its App ID and a
        private key must be added as secrets to the repo. The name of the secrets
        can be specified here.

        :param app_id_secret: 
        :param permissions: (experimental) The permissions granted to the token. Default: - all permissions granted to the app
        :param private_key_secret: 

        :default: - app id stored in "PROJEN_APP_ID" and private key stored in "PROJEN_APP_PRIVATE_KEY" with all permissions attached to the app

        :see: https://projen.io/github.html#github-app
        :stability: experimental
        '''
        options = GithubCredentialsAppOptions(
            app_id_secret=app_id_secret,
            permissions=permissions,
            private_key_secret=private_key_secret,
        )

        return typing.cast("GithubCredentials", jsii.sinvoke(cls, "fromApp", [options]))

    @jsii.member(jsii_name="fromPersonalAccessToken")
    @builtins.classmethod
    def from_personal_access_token(
        cls,
        *,
        secret: typing.Optional[builtins.str] = None,
    ) -> "GithubCredentials":
        '''(experimental) Provide API access through a GitHub personal access token.

        The token must be added as a secret to the GitHub repo, and the name of the
        secret can be specified here.

        :param secret: 

        :default: - a secret named "PROJEN_GITHUB_TOKEN"

        :see: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
        :stability: experimental
        '''
        options = GithubCredentialsPersonalAccessTokenOptions(secret=secret)

        return typing.cast("GithubCredentials", jsii.sinvoke(cls, "fromPersonalAccessToken", [options]))

    @builtins.property
    @jsii.member(jsii_name="setupSteps")
    def setup_steps(self) -> typing.List[_JobStep_c3287c05]:
        '''(experimental) Setup steps to obtain GitHub credentials.

        :stability: experimental
        '''
        return typing.cast(typing.List[_JobStep_c3287c05], jsii.get(self, "setupSteps"))

    @builtins.property
    @jsii.member(jsii_name="tokenRef")
    def token_ref(self) -> builtins.str:
        '''(experimental) The value to use in a workflow when a GitHub token is expected.

        This
        typically looks like "${{ some.path.to.a.value }}".

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "tokenRef"))


@jsii.data_type(
    jsii_type="projen.github.GithubCredentialsAppOptions",
    jsii_struct_bases=[],
    name_mapping={
        "app_id_secret": "appIdSecret",
        "permissions": "permissions",
        "private_key_secret": "privateKeySecret",
    },
)
class GithubCredentialsAppOptions:
    def __init__(
        self,
        *,
        app_id_secret: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[typing.Union[_AppPermissions_59709d51, typing.Dict[builtins.str, typing.Any]]] = None,
        private_key_secret: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Options for ``GithubCredentials.fromApp``.

        :param app_id_secret: 
        :param permissions: (experimental) The permissions granted to the token. Default: - all permissions granted to the app
        :param private_key_secret: 

        :stability: experimental
        '''
        if isinstance(permissions, dict):
            permissions = _AppPermissions_59709d51(**permissions)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfe552d6288d1f706792afe5f041e666db050b8d0d3bb7062899a3bdefe652a8)
            check_type(argname="argument app_id_secret", value=app_id_secret, expected_type=type_hints["app_id_secret"])
            check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
            check_type(argname="argument private_key_secret", value=private_key_secret, expected_type=type_hints["private_key_secret"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if app_id_secret is not None:
            self._values["app_id_secret"] = app_id_secret
        if permissions is not None:
            self._values["permissions"] = permissions
        if private_key_secret is not None:
            self._values["private_key_secret"] = private_key_secret

    @builtins.property
    def app_id_secret(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("app_id_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissions(self) -> typing.Optional[_AppPermissions_59709d51]:
        '''(experimental) The permissions granted to the token.

        :default: - all permissions granted to the app

        :stability: experimental
        '''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[_AppPermissions_59709d51], result)

    @builtins.property
    def private_key_secret(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("private_key_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GithubCredentialsAppOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.github.GithubCredentialsPersonalAccessTokenOptions",
    jsii_struct_bases=[],
    name_mapping={"secret": "secret"},
)
class GithubCredentialsPersonalAccessTokenOptions:
    def __init__(self, *, secret: typing.Optional[builtins.str] = None) -> None:
        '''(experimental) Options for ``GithubCredentials.fromPersonalAccessToken``.

        :param secret: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e78a929d8dcc77b9b129a8219f48eb2caa427b99d226997aadfbbccaaa8bbc1)
            check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if secret is not None:
            self._values["secret"] = secret

    @builtins.property
    def secret(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("secret")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GithubCredentialsPersonalAccessTokenOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GithubWorkflow(
    _Component_2b0ad27f,
    metaclass=jsii.JSIIMeta,
    jsii_type="projen.github.GithubWorkflow",
):
    '''(experimental) Workflow for GitHub.

    A workflow is a configurable automated process made up of one or more jobs.

    :see: https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions
    :stability: experimental
    '''

    def __init__(
        self,
        github: GitHub,
        name: builtins.str,
        *,
        concurrency: typing.Optional[builtins.str] = None,
        force: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param github: -
        :param name: -
        :param concurrency: (experimental) Concurrency ensures that only a single job or workflow using the same concurrency group will run at a time. Currently in beta. Default: - disabled
        :param force: (experimental) Force the creation of the workflow even if ``workflows`` is disabled in ``GitHub``. Default: false

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca4f375b4fda039fc4fb5b2f4ad26a9d1695085d170d2d76e6d720c7cc22d02a)
            check_type(argname="argument github", value=github, expected_type=type_hints["github"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        options = GithubWorkflowOptions(concurrency=concurrency, force=force)

        jsii.create(self.__class__, self, [github, name, options])

    @jsii.member(jsii_name="addJob")
    def add_job(
        self,
        id: builtins.str,
        job: typing.Union[typing.Union[_JobCallingReusableWorkflow_12ad1018, typing.Dict[builtins.str, typing.Any]], typing.Union[_Job_20ffcf45, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''(experimental) Adds a single job to the workflow.

        :param id: The job name (unique within the workflow).
        :param job: The job specification.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41cabee474513917adfff8f9da118269944812886b749e97c9b0d6a0c6b27c68)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument job", value=job, expected_type=type_hints["job"])
        return typing.cast(None, jsii.invoke(self, "addJob", [id, job]))

    @jsii.member(jsii_name="addJobs")
    def add_jobs(
        self,
        jobs: typing.Mapping[builtins.str, typing.Union[typing.Union[_JobCallingReusableWorkflow_12ad1018, typing.Dict[builtins.str, typing.Any]], typing.Union[_Job_20ffcf45, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''(experimental) Add jobs to the workflow.

        :param jobs: Jobs to add.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35b214ee606f61696719b92d704439e37a0a249e846714952fe087dd08b962c4)
            check_type(argname="argument jobs", value=jobs, expected_type=type_hints["jobs"])
        return typing.cast(None, jsii.invoke(self, "addJobs", [jobs]))

    @jsii.member(jsii_name="on")
    def on(
        self,
        *,
        branch_protection_rule: typing.Optional[typing.Union[_BranchProtectionRuleOptions_422f7f4e, typing.Dict[builtins.str, typing.Any]]] = None,
        check_run: typing.Optional[typing.Union[_CheckRunOptions_66af1ceb, typing.Dict[builtins.str, typing.Any]]] = None,
        check_suite: typing.Optional[typing.Union[_CheckSuiteOptions_6a122376, typing.Dict[builtins.str, typing.Any]]] = None,
        create: typing.Optional[typing.Union[_CreateOptions_6247308d, typing.Dict[builtins.str, typing.Any]]] = None,
        delete: typing.Optional[typing.Union[_DeleteOptions_c46578d4, typing.Dict[builtins.str, typing.Any]]] = None,
        deployment: typing.Optional[typing.Union[_DeploymentOptions_0bea6580, typing.Dict[builtins.str, typing.Any]]] = None,
        deployment_status: typing.Optional[typing.Union[_DeploymentStatusOptions_f9cbd32b, typing.Dict[builtins.str, typing.Any]]] = None,
        discussion: typing.Optional[typing.Union[_DiscussionOptions_6b34c7b6, typing.Dict[builtins.str, typing.Any]]] = None,
        discussion_comment: typing.Optional[typing.Union[_DiscussionCommentOptions_e8674c31, typing.Dict[builtins.str, typing.Any]]] = None,
        fork: typing.Optional[typing.Union[_ForkOptions_0437229d, typing.Dict[builtins.str, typing.Any]]] = None,
        gollum: typing.Optional[typing.Union[_GollumOptions_1acffea2, typing.Dict[builtins.str, typing.Any]]] = None,
        issue_comment: typing.Optional[typing.Union[_IssueCommentOptions_b551b1e5, typing.Dict[builtins.str, typing.Any]]] = None,
        issues: typing.Optional[typing.Union[_IssuesOptions_dd89885c, typing.Dict[builtins.str, typing.Any]]] = None,
        label: typing.Optional[typing.Union[_LabelOptions_ca474a61, typing.Dict[builtins.str, typing.Any]]] = None,
        merge_group: typing.Optional[typing.Union[_MergeGroupOptions_683d3a61, typing.Dict[builtins.str, typing.Any]]] = None,
        milestone: typing.Optional[typing.Union[_MilestoneOptions_6f9d8b6f, typing.Dict[builtins.str, typing.Any]]] = None,
        page_build: typing.Optional[typing.Union[_PageBuildOptions_c30eafce, typing.Dict[builtins.str, typing.Any]]] = None,
        project: typing.Optional[typing.Union[_ProjectOptions_50d963ea, typing.Dict[builtins.str, typing.Any]]] = None,
        project_card: typing.Optional[typing.Union[_ProjectCardOptions_c89fc28d, typing.Dict[builtins.str, typing.Any]]] = None,
        project_column: typing.Optional[typing.Union[_ProjectColumnOptions_25a462f6, typing.Dict[builtins.str, typing.Any]]] = None,
        public: typing.Optional[typing.Union[_PublicOptions_2c3a3b94, typing.Dict[builtins.str, typing.Any]]] = None,
        pull_request: typing.Optional[typing.Union[_PullRequestOptions_b051b0c9, typing.Dict[builtins.str, typing.Any]]] = None,
        pull_request_review: typing.Optional[typing.Union[_PullRequestReviewOptions_27fd8e95, typing.Dict[builtins.str, typing.Any]]] = None,
        pull_request_review_comment: typing.Optional[typing.Union[_PullRequestReviewCommentOptions_85235a68, typing.Dict[builtins.str, typing.Any]]] = None,
        pull_request_target: typing.Optional[typing.Union[_PullRequestTargetOptions_81011bb1, typing.Dict[builtins.str, typing.Any]]] = None,
        push: typing.Optional[typing.Union[_PushOptions_63e1c4f2, typing.Dict[builtins.str, typing.Any]]] = None,
        registry_package: typing.Optional[typing.Union[_RegistryPackageOptions_781d5ac7, typing.Dict[builtins.str, typing.Any]]] = None,
        release: typing.Optional[typing.Union[_ReleaseOptions_d152186d, typing.Dict[builtins.str, typing.Any]]] = None,
        repository_dispatch: typing.Optional[typing.Union[_RepositoryDispatchOptions_d75e9903, typing.Dict[builtins.str, typing.Any]]] = None,
        schedule: typing.Optional[typing.Sequence[typing.Union[_CronScheduleOptions_7724cd93, typing.Dict[builtins.str, typing.Any]]]] = None,
        status: typing.Optional[typing.Union[_StatusOptions_aa35df44, typing.Dict[builtins.str, typing.Any]]] = None,
        watch: typing.Optional[typing.Union[_WatchOptions_d33f5d00, typing.Dict[builtins.str, typing.Any]]] = None,
        workflow_call: typing.Optional[typing.Union[_WorkflowCallOptions_bc57a5b4, typing.Dict[builtins.str, typing.Any]]] = None,
        workflow_dispatch: typing.Optional[typing.Union[_WorkflowDispatchOptions_7110ffdc, typing.Dict[builtins.str, typing.Any]]] = None,
        workflow_run: typing.Optional[typing.Union[_WorkflowRunOptions_5a4262c5, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''(experimental) Add events to triggers the workflow.

        :param branch_protection_rule: (experimental) Runs your workflow anytime the branch_protection_rule event occurs.
        :param check_run: (experimental) Runs your workflow anytime the check_run event occurs.
        :param check_suite: (experimental) Runs your workflow anytime the check_suite event occurs.
        :param create: (experimental) Runs your workflow anytime someone creates a branch or tag, which triggers the create event.
        :param delete: (experimental) Runs your workflow anytime someone deletes a branch or tag, which triggers the delete event.
        :param deployment: (experimental) Runs your workflow anytime someone creates a deployment, which triggers the deployment event. Deployments created with a commit SHA may not have a Git ref.
        :param deployment_status: (experimental) Runs your workflow anytime a third party provides a deployment status, which triggers the deployment_status event. Deployments created with a commit SHA may not have a Git ref.
        :param discussion: (experimental) Runs your workflow anytime the discussion event occurs. More than one activity type triggers this event.
        :param discussion_comment: (experimental) Runs your workflow anytime the discussion_comment event occurs. More than one activity type triggers this event.
        :param fork: (experimental) Runs your workflow anytime when someone forks a repository, which triggers the fork event.
        :param gollum: (experimental) Runs your workflow when someone creates or updates a Wiki page, which triggers the gollum event.
        :param issue_comment: (experimental) Runs your workflow anytime the issue_comment event occurs.
        :param issues: (experimental) Runs your workflow anytime the issues event occurs.
        :param label: (experimental) Runs your workflow anytime the label event occurs.
        :param merge_group: (experimental) Runs your workflow when a pull request is added to a merge queue, which adds the pull request to a merge group.
        :param milestone: (experimental) Runs your workflow anytime the milestone event occurs.
        :param page_build: (experimental) Runs your workflow anytime someone pushes to a GitHub Pages-enabled branch, which triggers the page_build event.
        :param project: (experimental) Runs your workflow anytime the project event occurs.
        :param project_card: (experimental) Runs your workflow anytime the project_card event occurs.
        :param project_column: (experimental) Runs your workflow anytime the project_column event occurs.
        :param public: (experimental) Runs your workflow anytime someone makes a private repository public, which triggers the public event.
        :param pull_request: (experimental) Runs your workflow anytime the pull_request event occurs.
        :param pull_request_review: (experimental) Runs your workflow anytime the pull_request_review event occurs.
        :param pull_request_review_comment: (experimental) Runs your workflow anytime a comment on a pull request's unified diff is modified, which triggers the pull_request_review_comment event.
        :param pull_request_target: (experimental) This event runs in the context of the base of the pull request, rather than in the merge commit as the pull_request event does. This prevents executing unsafe workflow code from the head of the pull request that could alter your repository or steal any secrets you use in your workflow. This event allows you to do things like create workflows that label and comment on pull requests based on the contents of the event payload. WARNING: The ``pull_request_target`` event is granted read/write repository token and can access secrets, even when it is triggered from a fork. Although the workflow runs in the context of the base of the pull request, you should make sure that you do not check out, build, or run untrusted code from the pull request with this event. Additionally, any caches share the same scope as the base branch, and to help prevent cache poisoning, you should not save the cache if there is a possibility that the cache contents were altered.
        :param push: (experimental) Runs your workflow when someone pushes to a repository branch, which triggers the push event.
        :param registry_package: (experimental) Runs your workflow anytime a package is published or updated.
        :param release: (experimental) Runs your workflow anytime the release event occurs.
        :param repository_dispatch: (experimental) You can use the GitHub API to trigger a webhook event called repository_dispatch when you want to trigger a workflow for activity that happens outside of GitHub.
        :param schedule: (experimental) You can schedule a workflow to run at specific UTC times using POSIX cron syntax. Scheduled workflows run on the latest commit on the default or base branch. The shortest interval you can run scheduled workflows is once every 5 minutes.
        :param status: (experimental) Runs your workflow anytime the status of a Git commit changes, which triggers the status event.
        :param watch: (experimental) Runs your workflow anytime the watch event occurs.
        :param workflow_call: (experimental) Can be called from another workflow.
        :param workflow_dispatch: (experimental) You can configure custom-defined input properties, default input values, and required inputs for the event directly in your workflow. When the workflow runs, you can access the input values in the github.event.inputs context.
        :param workflow_run: (experimental) This event occurs when a workflow run is requested or completed, and allows you to execute a workflow based on the finished result of another workflow. A workflow run is triggered regardless of the result of the previous workflow.

        :stability: experimental
        '''
        events = _Triggers_e9ae7617(
            branch_protection_rule=branch_protection_rule,
            check_run=check_run,
            check_suite=check_suite,
            create=create,
            delete=delete,
            deployment=deployment,
            deployment_status=deployment_status,
            discussion=discussion,
            discussion_comment=discussion_comment,
            fork=fork,
            gollum=gollum,
            issue_comment=issue_comment,
            issues=issues,
            label=label,
            merge_group=merge_group,
            milestone=milestone,
            page_build=page_build,
            project=project,
            project_card=project_card,
            project_column=project_column,
            public=public,
            pull_request=pull_request,
            pull_request_review=pull_request_review,
            pull_request_review_comment=pull_request_review_comment,
            pull_request_target=pull_request_target,
            push=push,
            registry_package=registry_package,
            release=release,
            repository_dispatch=repository_dispatch,
            schedule=schedule,
            status=status,
            watch=watch,
            workflow_call=workflow_call,
            workflow_dispatch=workflow_dispatch,
            workflow_run=workflow_run,
        )

        return typing.cast(None, jsii.invoke(self, "on", [events]))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''(experimental) The name of the workflow.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="projenCredentials")
    def projen_credentials(self) -> GithubCredentials:
        '''(experimental) GitHub API authentication method used by projen workflows.

        :stability: experimental
        '''
        return typing.cast(GithubCredentials, jsii.get(self, "projenCredentials"))

    @builtins.property
    @jsii.member(jsii_name="concurrency")
    def concurrency(self) -> typing.Optional[builtins.str]:
        '''(experimental) Concurrency ensures that only a single job or workflow using the same concurrency group will run at a time.

        :default: disabled

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "concurrency"))

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(self) -> typing.Optional[_YamlFile_909731b0]:
        '''(experimental) The workflow YAML file.

        May not exist if ``workflowsEnabled`` is false on ``GitHub``.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[_YamlFile_909731b0], jsii.get(self, "file"))

    @builtins.property
    @jsii.member(jsii_name="runName")
    def run_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name for workflow runs generated from the workflow.

        GitHub displays the
        workflow run name in the list of workflow runs on your repository's
        "Actions" tab. If ``run-name`` is omitted or is only whitespace, then the run
        name is set to event-specific information for the workflow run. For
        example, for a workflow triggered by a ``push`` or ``pull_request`` event, it
        is set as the commit message.

        This value can include expressions and can reference ``github`` and ``inputs``
        contexts.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runName"))

    @run_name.setter
    def run_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6273080200c7722c9774364ee8460bccd3337cd48edc420530ca75f7c2974d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runName", value)


@jsii.data_type(
    jsii_type="projen.github.GithubWorkflowOptions",
    jsii_struct_bases=[],
    name_mapping={"concurrency": "concurrency", "force": "force"},
)
class GithubWorkflowOptions:
    def __init__(
        self,
        *,
        concurrency: typing.Optional[builtins.str] = None,
        force: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Options for ``GithubWorkflow``.

        :param concurrency: (experimental) Concurrency ensures that only a single job or workflow using the same concurrency group will run at a time. Currently in beta. Default: - disabled
        :param force: (experimental) Force the creation of the workflow even if ``workflows`` is disabled in ``GitHub``. Default: false

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c779b00d3df0cff3a9570cc6ed35339952399a898d5854423c3329b55bf736ec)
            check_type(argname="argument concurrency", value=concurrency, expected_type=type_hints["concurrency"])
            check_type(argname="argument force", value=force, expected_type=type_hints["force"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if concurrency is not None:
            self._values["concurrency"] = concurrency
        if force is not None:
            self._values["force"] = force

    @builtins.property
    def concurrency(self) -> typing.Optional[builtins.str]:
        '''(experimental) Concurrency ensures that only a single job or workflow using the same concurrency group will run at a time.

        Currently in beta.

        :default: - disabled

        :see: https://docs.github.com/en/actions/learn-github-actions/workflow-syntax-for-github-actions#concurrency
        :stability: experimental
        '''
        result = self._values.get("concurrency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def force(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Force the creation of the workflow even if ``workflows`` is disabled in ``GitHub``.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("force")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GithubWorkflowOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="projen.github.IAddConditionsLater")
class IAddConditionsLater(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    @jsii.member(jsii_name="render")
    def render(self) -> typing.List[builtins.str]:
        '''
        :stability: experimental
        '''
        ...


class _IAddConditionsLaterProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "projen.github.IAddConditionsLater"

    @jsii.member(jsii_name="render")
    def render(self) -> typing.List[builtins.str]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "render", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAddConditionsLater).__jsii_proxy_class__ = lambda : _IAddConditionsLaterProxy


class Mergify(
    _Component_2b0ad27f,
    metaclass=jsii.JSIIMeta,
    jsii_type="projen.github.Mergify",
):
    '''
    :stability: experimental
    '''

    def __init__(
        self,
        github: GitHub,
        *,
        queues: typing.Optional[typing.Sequence[typing.Union["MergifyQueue", typing.Dict[builtins.str, typing.Any]]]] = None,
        rules: typing.Optional[typing.Sequence[typing.Union["MergifyRule", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param github: -
        :param queues: 
        :param rules: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98cefc8f23feb67fa3f26fe0afa2490919ec4c7078182e46e92ccd4220389a8c)
            check_type(argname="argument github", value=github, expected_type=type_hints["github"])
        options = MergifyOptions(queues=queues, rules=rules)

        jsii.create(self.__class__, self, [github, options])

    @jsii.member(jsii_name="addQueue")
    def add_queue(
        self,
        *,
        conditions: typing.Sequence[typing.Union[builtins.str, typing.Union["MergifyConditionalOperator", typing.Dict[builtins.str, typing.Any]]]],
        name: builtins.str,
    ) -> None:
        '''
        :param conditions: (experimental) A list of Conditions string that must match against the pull request for the pull request to be added to the queue.
        :param name: (experimental) The name of the queue.

        :stability: experimental
        '''
        queue = MergifyQueue(conditions=conditions, name=name)

        return typing.cast(None, jsii.invoke(self, "addQueue", [queue]))

    @jsii.member(jsii_name="addRule")
    def add_rule(
        self,
        *,
        actions: typing.Mapping[builtins.str, typing.Any],
        conditions: typing.Sequence[typing.Union[builtins.str, typing.Union["MergifyConditionalOperator", typing.Dict[builtins.str, typing.Any]]]],
        name: builtins.str,
    ) -> None:
        '''
        :param actions: (experimental) A dictionary made of Actions that will be executed on the matching pull requests.
        :param conditions: (experimental) A list of Conditions string that must match against the pull request for the rule to be applied.
        :param name: (experimental) The name of the rule. This is not used by the engine directly, but is used when reporting information about a rule.

        :stability: experimental
        '''
        rule = MergifyRule(actions=actions, conditions=conditions, name=name)

        return typing.cast(None, jsii.invoke(self, "addRule", [rule]))


@jsii.data_type(
    jsii_type="projen.github.MergifyConditionalOperator",
    jsii_struct_bases=[],
    name_mapping={"and_": "and", "or_": "or"},
)
class MergifyConditionalOperator:
    def __init__(
        self,
        *,
        and_: typing.Optional[typing.Sequence[typing.Union[builtins.str, typing.Union["MergifyConditionalOperator", typing.Dict[builtins.str, typing.Any]]]]] = None,
        or_: typing.Optional[typing.Sequence[typing.Union[builtins.str, typing.Union["MergifyConditionalOperator", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''(experimental) The Mergify conditional operators that can be used are: ``or`` and ``and``.

        Note: The number of nested conditions is limited to 3.

        :param and_: 
        :param or_: 

        :see: https://docs.mergify.io/conditions/#combining-conditions-with-operators
        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c18537aa65489dcd3a6af1268daa4ec994e84f0720a3e846460acbcbf8e1474d)
            check_type(argname="argument and_", value=and_, expected_type=type_hints["and_"])
            check_type(argname="argument or_", value=or_, expected_type=type_hints["or_"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if and_ is not None:
            self._values["and_"] = and_
        if or_ is not None:
            self._values["or_"] = or_

    @builtins.property
    def and_(
        self,
    ) -> typing.Optional[typing.List[typing.Union[builtins.str, "MergifyConditionalOperator"]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("and_")
        return typing.cast(typing.Optional[typing.List[typing.Union[builtins.str, "MergifyConditionalOperator"]]], result)

    @builtins.property
    def or_(
        self,
    ) -> typing.Optional[typing.List[typing.Union[builtins.str, "MergifyConditionalOperator"]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("or_")
        return typing.cast(typing.Optional[typing.List[typing.Union[builtins.str, "MergifyConditionalOperator"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MergifyConditionalOperator(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.github.MergifyOptions",
    jsii_struct_bases=[],
    name_mapping={"queues": "queues", "rules": "rules"},
)
class MergifyOptions:
    def __init__(
        self,
        *,
        queues: typing.Optional[typing.Sequence[typing.Union["MergifyQueue", typing.Dict[builtins.str, typing.Any]]]] = None,
        rules: typing.Optional[typing.Sequence[typing.Union["MergifyRule", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param queues: 
        :param rules: 

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__527734fcd5357c536553ff5f47fe5062b93958305a451f587c870879e4f2c441)
            check_type(argname="argument queues", value=queues, expected_type=type_hints["queues"])
            check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if queues is not None:
            self._values["queues"] = queues
        if rules is not None:
            self._values["rules"] = rules

    @builtins.property
    def queues(self) -> typing.Optional[typing.List["MergifyQueue"]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("queues")
        return typing.cast(typing.Optional[typing.List["MergifyQueue"]], result)

    @builtins.property
    def rules(self) -> typing.Optional[typing.List["MergifyRule"]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("rules")
        return typing.cast(typing.Optional[typing.List["MergifyRule"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MergifyOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.github.MergifyQueue",
    jsii_struct_bases=[],
    name_mapping={"conditions": "conditions", "name": "name"},
)
class MergifyQueue:
    def __init__(
        self,
        *,
        conditions: typing.Sequence[typing.Union[builtins.str, typing.Union[MergifyConditionalOperator, typing.Dict[builtins.str, typing.Any]]]],
        name: builtins.str,
    ) -> None:
        '''
        :param conditions: (experimental) A list of Conditions string that must match against the pull request for the pull request to be added to the queue.
        :param name: (experimental) The name of the queue.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0471efd0a49bc64e556512e765a1df23d4a975f26cb6de765579b4173907f467)
            check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "conditions": conditions,
            "name": name,
        }

    @builtins.property
    def conditions(
        self,
    ) -> typing.List[typing.Union[builtins.str, MergifyConditionalOperator]]:
        '''(experimental) A list of Conditions string that must match against the pull request for the pull request to be added to the queue.

        :see: https://docs.mergify.com/conditions/#conditions
        :stability: experimental
        '''
        result = self._values.get("conditions")
        assert result is not None, "Required property 'conditions' is missing"
        return typing.cast(typing.List[typing.Union[builtins.str, MergifyConditionalOperator]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''(experimental) The name of the queue.

        :stability: experimental
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MergifyQueue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.github.MergifyRule",
    jsii_struct_bases=[],
    name_mapping={"actions": "actions", "conditions": "conditions", "name": "name"},
)
class MergifyRule:
    def __init__(
        self,
        *,
        actions: typing.Mapping[builtins.str, typing.Any],
        conditions: typing.Sequence[typing.Union[builtins.str, typing.Union[MergifyConditionalOperator, typing.Dict[builtins.str, typing.Any]]]],
        name: builtins.str,
    ) -> None:
        '''
        :param actions: (experimental) A dictionary made of Actions that will be executed on the matching pull requests.
        :param conditions: (experimental) A list of Conditions string that must match against the pull request for the rule to be applied.
        :param name: (experimental) The name of the rule. This is not used by the engine directly, but is used when reporting information about a rule.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95405391335691b357d88cc73d37d1ee20fceae6cf671811812f639729b5accd)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "actions": actions,
            "conditions": conditions,
            "name": name,
        }

    @builtins.property
    def actions(self) -> typing.Mapping[builtins.str, typing.Any]:
        '''(experimental) A dictionary made of Actions that will be executed on the matching pull requests.

        :see: https://docs.mergify.io/actions/#actions
        :stability: experimental
        '''
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return typing.cast(typing.Mapping[builtins.str, typing.Any], result)

    @builtins.property
    def conditions(
        self,
    ) -> typing.List[typing.Union[builtins.str, MergifyConditionalOperator]]:
        '''(experimental) A list of Conditions string that must match against the pull request for the rule to be applied.

        :see: https://docs.mergify.io/conditions/#conditions
        :stability: experimental
        '''
        result = self._values.get("conditions")
        assert result is not None, "Required property 'conditions' is missing"
        return typing.cast(typing.List[typing.Union[builtins.str, MergifyConditionalOperator]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''(experimental) The name of the rule.

        This is not used by the engine directly,
        but is used when reporting information about a rule.

        :stability: experimental
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MergifyRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PullRequestLint(
    _Component_2b0ad27f,
    metaclass=jsii.JSIIMeta,
    jsii_type="projen.github.PullRequestLint",
):
    '''(experimental) Configure validations to run on GitHub pull requests.

    Only generates a file if at least one linter is configured.

    :stability: experimental
    '''

    def __init__(
        self,
        github: GitHub,
        *,
        runs_on: typing.Optional[typing.Sequence[builtins.str]] = None,
        semantic_title: typing.Optional[builtins.bool] = None,
        semantic_title_options: typing.Optional[typing.Union["SemanticTitleOptions", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param github: -
        :param runs_on: (experimental) Github Runner selection labels. Default: ["ubuntu-latest"]
        :param semantic_title: (experimental) Validate that pull request titles follow Conventional Commits. Default: true
        :param semantic_title_options: (experimental) Options for validating the conventional commit title linter. Default: - title must start with "feat", "fix", or "chore"

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e947e718bf3d7bd85f25ecd7154aeef36d789ef76012c5d50b8c1a265be7750)
            check_type(argname="argument github", value=github, expected_type=type_hints["github"])
        options = PullRequestLintOptions(
            runs_on=runs_on,
            semantic_title=semantic_title,
            semantic_title_options=semantic_title_options,
        )

        jsii.create(self.__class__, self, [github, options])


@jsii.data_type(
    jsii_type="projen.github.PullRequestLintOptions",
    jsii_struct_bases=[],
    name_mapping={
        "runs_on": "runsOn",
        "semantic_title": "semanticTitle",
        "semantic_title_options": "semanticTitleOptions",
    },
)
class PullRequestLintOptions:
    def __init__(
        self,
        *,
        runs_on: typing.Optional[typing.Sequence[builtins.str]] = None,
        semantic_title: typing.Optional[builtins.bool] = None,
        semantic_title_options: typing.Optional[typing.Union["SemanticTitleOptions", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''(experimental) Options for PullRequestLint.

        :param runs_on: (experimental) Github Runner selection labels. Default: ["ubuntu-latest"]
        :param semantic_title: (experimental) Validate that pull request titles follow Conventional Commits. Default: true
        :param semantic_title_options: (experimental) Options for validating the conventional commit title linter. Default: - title must start with "feat", "fix", or "chore"

        :stability: experimental
        '''
        if isinstance(semantic_title_options, dict):
            semantic_title_options = SemanticTitleOptions(**semantic_title_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__753ecd53f4dea89ebcc13327977e141a051588fef5185d3f14e06f44f6c47a63)
            check_type(argname="argument runs_on", value=runs_on, expected_type=type_hints["runs_on"])
            check_type(argname="argument semantic_title", value=semantic_title, expected_type=type_hints["semantic_title"])
            check_type(argname="argument semantic_title_options", value=semantic_title_options, expected_type=type_hints["semantic_title_options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if runs_on is not None:
            self._values["runs_on"] = runs_on
        if semantic_title is not None:
            self._values["semantic_title"] = semantic_title
        if semantic_title_options is not None:
            self._values["semantic_title_options"] = semantic_title_options

    @builtins.property
    def runs_on(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) Github Runner selection labels.

        :default: ["ubuntu-latest"]

        :stability: experimental
        '''
        result = self._values.get("runs_on")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def semantic_title(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Validate that pull request titles follow Conventional Commits.

        :default: true

        :see: https://www.conventionalcommits.org/
        :stability: experimental
        '''
        result = self._values.get("semantic_title")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def semantic_title_options(self) -> typing.Optional["SemanticTitleOptions"]:
        '''(experimental) Options for validating the conventional commit title linter.

        :default: - title must start with "feat", "fix", or "chore"

        :stability: experimental
        '''
        result = self._values.get("semantic_title_options")
        return typing.cast(typing.Optional["SemanticTitleOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PullRequestLintOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PullRequestTemplate(
    _TextFile_4a74808c,
    metaclass=jsii.JSIIMeta,
    jsii_type="projen.github.PullRequestTemplate",
):
    '''(experimental) Template for GitHub pull requests.

    :stability: experimental
    '''

    def __init__(
        self,
        github: GitHub,
        *,
        lines: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param github: -
        :param lines: (experimental) The contents of the template. You can use ``addLine()`` to add additional lines. Default: - a standard default template will be created.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__609f06a532384d8ff817f7118dd1e021a8ee15a4aeb1b785b674a5c885fabc7b)
            check_type(argname="argument github", value=github, expected_type=type_hints["github"])
        options = PullRequestTemplateOptions(lines=lines)

        jsii.create(self.__class__, self, [github, options])


@jsii.data_type(
    jsii_type="projen.github.PullRequestTemplateOptions",
    jsii_struct_bases=[],
    name_mapping={"lines": "lines"},
)
class PullRequestTemplateOptions:
    def __init__(
        self,
        *,
        lines: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''(experimental) Options for ``PullRequestTemplate``.

        :param lines: (experimental) The contents of the template. You can use ``addLine()`` to add additional lines. Default: - a standard default template will be created.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8786063961cc00764e7c2005db60e7d427b8a81ce2275510888beb4eed1d1c6)
            check_type(argname="argument lines", value=lines, expected_type=type_hints["lines"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if lines is not None:
            self._values["lines"] = lines

    @builtins.property
    def lines(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) The contents of the template.

        You can use ``addLine()`` to add additional lines.

        :default: - a standard default template will be created.

        :stability: experimental
        '''
        result = self._values.get("lines")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PullRequestTemplateOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.github.SemanticTitleOptions",
    jsii_struct_bases=[],
    name_mapping={"require_scope": "requireScope", "types": "types"},
)
class SemanticTitleOptions:
    def __init__(
        self,
        *,
        require_scope: typing.Optional[builtins.bool] = None,
        types: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''(experimental) Options for linting that PR titles follow Conventional Commits.

        :param require_scope: (experimental) Configure that a scope must always be provided. e.g. feat(ui), fix(core) Default: false
        :param types: (experimental) Configure a list of commit types that are allowed. Default: ["feat", "fix", "chore"]

        :see: https://www.conventionalcommits.org/
        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d043d0484269cca19493b2d2d5c51f9cfe65a12520148f80ef37f6855457de0)
            check_type(argname="argument require_scope", value=require_scope, expected_type=type_hints["require_scope"])
            check_type(argname="argument types", value=types, expected_type=type_hints["types"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if require_scope is not None:
            self._values["require_scope"] = require_scope
        if types is not None:
            self._values["types"] = types

    @builtins.property
    def require_scope(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Configure that a scope must always be provided.

        e.g. feat(ui), fix(core)

        :default: false

        :stability: experimental
        '''
        result = self._values.get("require_scope")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) Configure a list of commit types that are allowed.

        :default: ["feat", "fix", "chore"]

        :stability: experimental
        '''
        result = self._values.get("types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SemanticTitleOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Stale(
    _Component_2b0ad27f,
    metaclass=jsii.JSIIMeta,
    jsii_type="projen.github.Stale",
):
    '''(experimental) Warns and then closes issues and PRs that have had no activity for a specified amount of time.

    The default configuration will:

    - Add a "Stale" label to pull requests after 14 days and closed after 2 days
    - Add a "Stale" label to issues after 60 days and closed after 7 days
    - If a comment is added, the label will be removed and timer is restarted.

    :see: https://github.com/actions/stale
    :stability: experimental
    '''

    def __init__(
        self,
        github: GitHub,
        *,
        issues: typing.Optional[typing.Union["StaleBehavior", typing.Dict[builtins.str, typing.Any]]] = None,
        pull_request: typing.Optional[typing.Union["StaleBehavior", typing.Dict[builtins.str, typing.Any]]] = None,
        runs_on: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param github: -
        :param issues: (experimental) How to handle stale issues. Default: - By default, stale issues with no activity will be marked as stale after 60 days and closed within 7 days.
        :param pull_request: (experimental) How to handle stale pull requests. Default: - By default, pull requests with no activity will be marked as stale after 14 days and closed within 2 days with relevant comments.
        :param runs_on: (experimental) Github Runner selection labels. Default: ["ubuntu-latest"]

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cde7a08a3b4ffe6754e0a55a7717404b9b4693c90412e433734959e936b1a9b8)
            check_type(argname="argument github", value=github, expected_type=type_hints["github"])
        options = StaleOptions(
            issues=issues, pull_request=pull_request, runs_on=runs_on
        )

        jsii.create(self.__class__, self, [github, options])


@jsii.data_type(
    jsii_type="projen.github.StaleBehavior",
    jsii_struct_bases=[],
    name_mapping={
        "close_message": "closeMessage",
        "days_before_close": "daysBeforeClose",
        "days_before_stale": "daysBeforeStale",
        "enabled": "enabled",
        "exempt_labels": "exemptLabels",
        "stale_label": "staleLabel",
        "stale_message": "staleMessage",
    },
)
class StaleBehavior:
    def __init__(
        self,
        *,
        close_message: typing.Optional[builtins.str] = None,
        days_before_close: typing.Optional[jsii.Number] = None,
        days_before_stale: typing.Optional[jsii.Number] = None,
        enabled: typing.Optional[builtins.bool] = None,
        exempt_labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        stale_label: typing.Optional[builtins.str] = None,
        stale_message: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Stale behavior.

        :param close_message: (experimental) The comment to add to the issue/PR when it's closed. Default: "Closing this pull request as it hasn't seen activity for a while. Please add a comment
        :param days_before_close: (experimental) Days until the issue/PR is closed after it is marked as "Stale". Set to -1 to disable. Default: -
        :param days_before_stale: (experimental) How many days until the issue or pull request is marked as "Stale". Set to -1 to disable. Default: -
        :param enabled: (experimental) Determines if this behavior is enabled. Same as setting ``daysBeforeStale`` and ``daysBeforeClose`` to ``-1``. Default: true
        :param exempt_labels: (experimental) Label which exempt an issue/PR from becoming stale. Set to ``[]`` to disable. Default: - ["backlog"]
        :param stale_label: (experimental) The label to apply to the issue/PR when it becomes stale. Default: "stale"
        :param stale_message: (experimental) The comment to add to the issue/PR when it becomes stale. Default: "This pull request is now marked as stale because hasn't seen activity for a while. Add a comment or it will be closed soon."

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14e82ddb43ce0bf58c1e751d8ad775da433271157f06eea21bcdab08f1f837f1)
            check_type(argname="argument close_message", value=close_message, expected_type=type_hints["close_message"])
            check_type(argname="argument days_before_close", value=days_before_close, expected_type=type_hints["days_before_close"])
            check_type(argname="argument days_before_stale", value=days_before_stale, expected_type=type_hints["days_before_stale"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument exempt_labels", value=exempt_labels, expected_type=type_hints["exempt_labels"])
            check_type(argname="argument stale_label", value=stale_label, expected_type=type_hints["stale_label"])
            check_type(argname="argument stale_message", value=stale_message, expected_type=type_hints["stale_message"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if close_message is not None:
            self._values["close_message"] = close_message
        if days_before_close is not None:
            self._values["days_before_close"] = days_before_close
        if days_before_stale is not None:
            self._values["days_before_stale"] = days_before_stale
        if enabled is not None:
            self._values["enabled"] = enabled
        if exempt_labels is not None:
            self._values["exempt_labels"] = exempt_labels
        if stale_label is not None:
            self._values["stale_label"] = stale_label
        if stale_message is not None:
            self._values["stale_message"] = stale_message

    @builtins.property
    def close_message(self) -> typing.Optional[builtins.str]:
        '''(experimental) The comment to add to the issue/PR when it's closed.

        :default: "Closing this pull request as it hasn't seen activity for a while. Please add a comment

        :stability: experimental
        :mentioning: a maintainer when you are ready to continue."
        '''
        result = self._values.get("close_message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def days_before_close(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Days until the issue/PR is closed after it is marked as "Stale".

        Set to -1 to disable.

        :default: -

        :stability: experimental
        '''
        result = self._values.get("days_before_close")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def days_before_stale(self) -> typing.Optional[jsii.Number]:
        '''(experimental) How many days until the issue or pull request is marked as "Stale".

        Set to -1 to disable.

        :default: -

        :stability: experimental
        '''
        result = self._values.get("days_before_stale")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Determines if this behavior is enabled.

        Same as setting ``daysBeforeStale`` and ``daysBeforeClose`` to ``-1``.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def exempt_labels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) Label which exempt an issue/PR from becoming stale.

        Set to ``[]`` to disable.

        :default: - ["backlog"]

        :stability: experimental
        '''
        result = self._values.get("exempt_labels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def stale_label(self) -> typing.Optional[builtins.str]:
        '''(experimental) The label to apply to the issue/PR when it becomes stale.

        :default: "stale"

        :stability: experimental
        '''
        result = self._values.get("stale_label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stale_message(self) -> typing.Optional[builtins.str]:
        '''(experimental) The comment to add to the issue/PR when it becomes stale.

        :default: "This pull request is now marked as stale because hasn't seen activity for a while. Add a comment or it will be closed soon."

        :stability: experimental
        '''
        result = self._values.get("stale_message")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StaleBehavior(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.github.StaleOptions",
    jsii_struct_bases=[],
    name_mapping={
        "issues": "issues",
        "pull_request": "pullRequest",
        "runs_on": "runsOn",
    },
)
class StaleOptions:
    def __init__(
        self,
        *,
        issues: typing.Optional[typing.Union[StaleBehavior, typing.Dict[builtins.str, typing.Any]]] = None,
        pull_request: typing.Optional[typing.Union[StaleBehavior, typing.Dict[builtins.str, typing.Any]]] = None,
        runs_on: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''(experimental) Options for ``Stale``.

        :param issues: (experimental) How to handle stale issues. Default: - By default, stale issues with no activity will be marked as stale after 60 days and closed within 7 days.
        :param pull_request: (experimental) How to handle stale pull requests. Default: - By default, pull requests with no activity will be marked as stale after 14 days and closed within 2 days with relevant comments.
        :param runs_on: (experimental) Github Runner selection labels. Default: ["ubuntu-latest"]

        :stability: experimental
        '''
        if isinstance(issues, dict):
            issues = StaleBehavior(**issues)
        if isinstance(pull_request, dict):
            pull_request = StaleBehavior(**pull_request)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3522ab5e4c43b16a792a120a46122600785f2af070bebc9421e03d5a3d80e371)
            check_type(argname="argument issues", value=issues, expected_type=type_hints["issues"])
            check_type(argname="argument pull_request", value=pull_request, expected_type=type_hints["pull_request"])
            check_type(argname="argument runs_on", value=runs_on, expected_type=type_hints["runs_on"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if issues is not None:
            self._values["issues"] = issues
        if pull_request is not None:
            self._values["pull_request"] = pull_request
        if runs_on is not None:
            self._values["runs_on"] = runs_on

    @builtins.property
    def issues(self) -> typing.Optional[StaleBehavior]:
        '''(experimental) How to handle stale issues.

        :default:

        - By default, stale issues with no activity will be marked as
        stale after 60 days and closed within 7 days.

        :stability: experimental
        '''
        result = self._values.get("issues")
        return typing.cast(typing.Optional[StaleBehavior], result)

    @builtins.property
    def pull_request(self) -> typing.Optional[StaleBehavior]:
        '''(experimental) How to handle stale pull requests.

        :default:

        - By default, pull requests with no activity will be marked as
        stale after 14 days and closed within 2 days with relevant comments.

        :stability: experimental
        '''
        result = self._values.get("pull_request")
        return typing.cast(typing.Optional[StaleBehavior], result)

    @builtins.property
    def runs_on(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) Github Runner selection labels.

        :default: ["ubuntu-latest"]

        :stability: experimental
        '''
        result = self._values.get("runs_on")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StaleOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TaskWorkflow(
    GithubWorkflow,
    metaclass=jsii.JSIIMeta,
    jsii_type="projen.github.TaskWorkflow",
):
    '''(experimental) A GitHub workflow for common build tasks within a project.

    :stability: experimental
    '''

    def __init__(
        self,
        github: GitHub,
        *,
        name: builtins.str,
        permissions: typing.Union[_JobPermissions_3b5b53dc, typing.Dict[builtins.str, typing.Any]],
        task: _Task_9fa875b6,
        artifacts_directory: typing.Optional[builtins.str] = None,
        checkout_with: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        condition: typing.Optional[builtins.str] = None,
        container: typing.Optional[typing.Union[_ContainerOptions_f50907af, typing.Dict[builtins.str, typing.Any]]] = None,
        env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        git_identity: typing.Optional[typing.Union[GitIdentity, typing.Dict[builtins.str, typing.Any]]] = None,
        job_id: typing.Optional[builtins.str] = None,
        outputs: typing.Optional[typing.Mapping[builtins.str, typing.Union[_JobStepOutput_acebe827, typing.Dict[builtins.str, typing.Any]]]] = None,
        post_build_steps: typing.Optional[typing.Sequence[typing.Union[_JobStep_c3287c05, typing.Dict[builtins.str, typing.Any]]]] = None,
        pre_build_steps: typing.Optional[typing.Sequence[typing.Union[_JobStep_c3287c05, typing.Dict[builtins.str, typing.Any]]]] = None,
        pre_checkout_steps: typing.Optional[typing.Sequence[typing.Union[_JobStep_c3287c05, typing.Dict[builtins.str, typing.Any]]]] = None,
        runs_on: typing.Optional[typing.Sequence[builtins.str]] = None,
        triggers: typing.Optional[typing.Union[_Triggers_e9ae7617, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param github: -
        :param name: (experimental) The workflow name.
        :param permissions: (experimental) Permissions for the build job.
        :param task: (experimental) The main task to be executed.
        :param artifacts_directory: (experimental) A directory name which contains artifacts to be uploaded (e.g. ``dist``). If this is set, the contents of this directory will be uploaded as an artifact at the end of the workflow run, even if other steps fail. Default: - not set
        :param checkout_with: (experimental) Override for the ``with`` property of the source code checkout step. Default: - not set
        :param condition: (experimental) Adds an 'if' condition to the workflow.
        :param container: Default: - default image
        :param env: (experimental) Workflow environment variables. Default: {}
        :param git_identity: (experimental) The git identity to use in this workflow.
        :param job_id: (experimental) The primary job id. Default: "build"
        :param outputs: (experimental) Mapping of job output names to values/expressions. Default: {}
        :param post_build_steps: (experimental) Actions to run after the main build step. Default: - not set
        :param pre_build_steps: (experimental) Steps to run before the main build step. Default: - not set
        :param pre_checkout_steps: (experimental) Initial steps to run before the source code checkout. Default: - not set
        :param runs_on: (experimental) Github Runner selection labels. Default: ["ubuntu-latest"]
        :param triggers: (experimental) The triggers for the workflow. Default: - by default workflows can only be triggered by manually.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d4fb3030e96a87b921aa6bfb0d4ccf7a90d4c2affbcb8eeca2d5a24c057601c)
            check_type(argname="argument github", value=github, expected_type=type_hints["github"])
        options = TaskWorkflowOptions(
            name=name,
            permissions=permissions,
            task=task,
            artifacts_directory=artifacts_directory,
            checkout_with=checkout_with,
            condition=condition,
            container=container,
            env=env,
            git_identity=git_identity,
            job_id=job_id,
            outputs=outputs,
            post_build_steps=post_build_steps,
            pre_build_steps=pre_build_steps,
            pre_checkout_steps=pre_checkout_steps,
            runs_on=runs_on,
            triggers=triggers,
        )

        jsii.create(self.__class__, self, [github, options])

    @builtins.property
    @jsii.member(jsii_name="jobId")
    def job_id(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "jobId"))

    @builtins.property
    @jsii.member(jsii_name="artifactsDirectory")
    def artifacts_directory(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "artifactsDirectory"))


@jsii.data_type(
    jsii_type="projen.github.TaskWorkflowOptions",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "permissions": "permissions",
        "task": "task",
        "artifacts_directory": "artifactsDirectory",
        "checkout_with": "checkoutWith",
        "condition": "condition",
        "container": "container",
        "env": "env",
        "git_identity": "gitIdentity",
        "job_id": "jobId",
        "outputs": "outputs",
        "post_build_steps": "postBuildSteps",
        "pre_build_steps": "preBuildSteps",
        "pre_checkout_steps": "preCheckoutSteps",
        "runs_on": "runsOn",
        "triggers": "triggers",
    },
)
class TaskWorkflowOptions:
    def __init__(
        self,
        *,
        name: builtins.str,
        permissions: typing.Union[_JobPermissions_3b5b53dc, typing.Dict[builtins.str, typing.Any]],
        task: _Task_9fa875b6,
        artifacts_directory: typing.Optional[builtins.str] = None,
        checkout_with: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        condition: typing.Optional[builtins.str] = None,
        container: typing.Optional[typing.Union[_ContainerOptions_f50907af, typing.Dict[builtins.str, typing.Any]]] = None,
        env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        git_identity: typing.Optional[typing.Union[GitIdentity, typing.Dict[builtins.str, typing.Any]]] = None,
        job_id: typing.Optional[builtins.str] = None,
        outputs: typing.Optional[typing.Mapping[builtins.str, typing.Union[_JobStepOutput_acebe827, typing.Dict[builtins.str, typing.Any]]]] = None,
        post_build_steps: typing.Optional[typing.Sequence[typing.Union[_JobStep_c3287c05, typing.Dict[builtins.str, typing.Any]]]] = None,
        pre_build_steps: typing.Optional[typing.Sequence[typing.Union[_JobStep_c3287c05, typing.Dict[builtins.str, typing.Any]]]] = None,
        pre_checkout_steps: typing.Optional[typing.Sequence[typing.Union[_JobStep_c3287c05, typing.Dict[builtins.str, typing.Any]]]] = None,
        runs_on: typing.Optional[typing.Sequence[builtins.str]] = None,
        triggers: typing.Optional[typing.Union[_Triggers_e9ae7617, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: (experimental) The workflow name.
        :param permissions: (experimental) Permissions for the build job.
        :param task: (experimental) The main task to be executed.
        :param artifacts_directory: (experimental) A directory name which contains artifacts to be uploaded (e.g. ``dist``). If this is set, the contents of this directory will be uploaded as an artifact at the end of the workflow run, even if other steps fail. Default: - not set
        :param checkout_with: (experimental) Override for the ``with`` property of the source code checkout step. Default: - not set
        :param condition: (experimental) Adds an 'if' condition to the workflow.
        :param container: Default: - default image
        :param env: (experimental) Workflow environment variables. Default: {}
        :param git_identity: (experimental) The git identity to use in this workflow.
        :param job_id: (experimental) The primary job id. Default: "build"
        :param outputs: (experimental) Mapping of job output names to values/expressions. Default: {}
        :param post_build_steps: (experimental) Actions to run after the main build step. Default: - not set
        :param pre_build_steps: (experimental) Steps to run before the main build step. Default: - not set
        :param pre_checkout_steps: (experimental) Initial steps to run before the source code checkout. Default: - not set
        :param runs_on: (experimental) Github Runner selection labels. Default: ["ubuntu-latest"]
        :param triggers: (experimental) The triggers for the workflow. Default: - by default workflows can only be triggered by manually.

        :stability: experimental
        '''
        if isinstance(permissions, dict):
            permissions = _JobPermissions_3b5b53dc(**permissions)
        if isinstance(container, dict):
            container = _ContainerOptions_f50907af(**container)
        if isinstance(git_identity, dict):
            git_identity = GitIdentity(**git_identity)
        if isinstance(triggers, dict):
            triggers = _Triggers_e9ae7617(**triggers)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15e1c594f5876baf2e105789fcb541bcb5e71cea5ad4320fb67052a9ce6946a8)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
            check_type(argname="argument task", value=task, expected_type=type_hints["task"])
            check_type(argname="argument artifacts_directory", value=artifacts_directory, expected_type=type_hints["artifacts_directory"])
            check_type(argname="argument checkout_with", value=checkout_with, expected_type=type_hints["checkout_with"])
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
            check_type(argname="argument container", value=container, expected_type=type_hints["container"])
            check_type(argname="argument env", value=env, expected_type=type_hints["env"])
            check_type(argname="argument git_identity", value=git_identity, expected_type=type_hints["git_identity"])
            check_type(argname="argument job_id", value=job_id, expected_type=type_hints["job_id"])
            check_type(argname="argument outputs", value=outputs, expected_type=type_hints["outputs"])
            check_type(argname="argument post_build_steps", value=post_build_steps, expected_type=type_hints["post_build_steps"])
            check_type(argname="argument pre_build_steps", value=pre_build_steps, expected_type=type_hints["pre_build_steps"])
            check_type(argname="argument pre_checkout_steps", value=pre_checkout_steps, expected_type=type_hints["pre_checkout_steps"])
            check_type(argname="argument runs_on", value=runs_on, expected_type=type_hints["runs_on"])
            check_type(argname="argument triggers", value=triggers, expected_type=type_hints["triggers"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "permissions": permissions,
            "task": task,
        }
        if artifacts_directory is not None:
            self._values["artifacts_directory"] = artifacts_directory
        if checkout_with is not None:
            self._values["checkout_with"] = checkout_with
        if condition is not None:
            self._values["condition"] = condition
        if container is not None:
            self._values["container"] = container
        if env is not None:
            self._values["env"] = env
        if git_identity is not None:
            self._values["git_identity"] = git_identity
        if job_id is not None:
            self._values["job_id"] = job_id
        if outputs is not None:
            self._values["outputs"] = outputs
        if post_build_steps is not None:
            self._values["post_build_steps"] = post_build_steps
        if pre_build_steps is not None:
            self._values["pre_build_steps"] = pre_build_steps
        if pre_checkout_steps is not None:
            self._values["pre_checkout_steps"] = pre_checkout_steps
        if runs_on is not None:
            self._values["runs_on"] = runs_on
        if triggers is not None:
            self._values["triggers"] = triggers

    @builtins.property
    def name(self) -> builtins.str:
        '''(experimental) The workflow name.

        :stability: experimental
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def permissions(self) -> _JobPermissions_3b5b53dc:
        '''(experimental) Permissions for the build job.

        :stability: experimental
        '''
        result = self._values.get("permissions")
        assert result is not None, "Required property 'permissions' is missing"
        return typing.cast(_JobPermissions_3b5b53dc, result)

    @builtins.property
    def task(self) -> _Task_9fa875b6:
        '''(experimental) The main task to be executed.

        :stability: experimental
        '''
        result = self._values.get("task")
        assert result is not None, "Required property 'task' is missing"
        return typing.cast(_Task_9fa875b6, result)

    @builtins.property
    def artifacts_directory(self) -> typing.Optional[builtins.str]:
        '''(experimental) A directory name which contains artifacts to be uploaded (e.g. ``dist``). If this is set, the contents of this directory will be uploaded as an artifact at the end of the workflow run, even if other steps fail.

        :default: - not set

        :stability: experimental
        '''
        result = self._values.get("artifacts_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def checkout_with(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''(experimental) Override for the ``with`` property of the source code checkout step.

        :default: - not set

        :stability: experimental
        '''
        result = self._values.get("checkout_with")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def condition(self) -> typing.Optional[builtins.str]:
        '''(experimental) Adds an 'if' condition to the workflow.

        :stability: experimental
        '''
        result = self._values.get("condition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def container(self) -> typing.Optional[_ContainerOptions_f50907af]:
        '''
        :default: - default image

        :stability: experimental
        '''
        result = self._values.get("container")
        return typing.cast(typing.Optional[_ContainerOptions_f50907af], result)

    @builtins.property
    def env(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''(experimental) Workflow environment variables.

        :default: {}

        :stability: experimental
        '''
        result = self._values.get("env")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def git_identity(self) -> typing.Optional[GitIdentity]:
        '''(experimental) The git identity to use in this workflow.

        :stability: experimental
        '''
        result = self._values.get("git_identity")
        return typing.cast(typing.Optional[GitIdentity], result)

    @builtins.property
    def job_id(self) -> typing.Optional[builtins.str]:
        '''(experimental) The primary job id.

        :default: "build"

        :stability: experimental
        '''
        result = self._values.get("job_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def outputs(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, _JobStepOutput_acebe827]]:
        '''(experimental) Mapping of job output names to values/expressions.

        :default: {}

        :stability: experimental
        '''
        result = self._values.get("outputs")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, _JobStepOutput_acebe827]], result)

    @builtins.property
    def post_build_steps(self) -> typing.Optional[typing.List[_JobStep_c3287c05]]:
        '''(experimental) Actions to run after the main build step.

        :default: - not set

        :stability: experimental
        '''
        result = self._values.get("post_build_steps")
        return typing.cast(typing.Optional[typing.List[_JobStep_c3287c05]], result)

    @builtins.property
    def pre_build_steps(self) -> typing.Optional[typing.List[_JobStep_c3287c05]]:
        '''(experimental) Steps to run before the main build step.

        :default: - not set

        :stability: experimental
        '''
        result = self._values.get("pre_build_steps")
        return typing.cast(typing.Optional[typing.List[_JobStep_c3287c05]], result)

    @builtins.property
    def pre_checkout_steps(self) -> typing.Optional[typing.List[_JobStep_c3287c05]]:
        '''(experimental) Initial steps to run before the source code checkout.

        :default: - not set

        :stability: experimental
        '''
        result = self._values.get("pre_checkout_steps")
        return typing.cast(typing.Optional[typing.List[_JobStep_c3287c05]], result)

    @builtins.property
    def runs_on(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) Github Runner selection labels.

        :default: ["ubuntu-latest"]

        :stability: experimental
        '''
        result = self._values.get("runs_on")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def triggers(self) -> typing.Optional[_Triggers_e9ae7617]:
        '''(experimental) The triggers for the workflow.

        :default: - by default workflows can only be triggered by manually.

        :stability: experimental
        '''
        result = self._values.get("triggers")
        return typing.cast(typing.Optional[_Triggers_e9ae7617], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TaskWorkflowOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="projen.github.VersioningStrategy")
class VersioningStrategy(enum.Enum):
    '''(experimental) The strategy to use when edits manifest and lock files.

    :stability: experimental
    '''

    LOCKFILE_ONLY = "LOCKFILE_ONLY"
    '''(experimental) Only create pull requests to update lockfiles updates.

    Ignore any new
    versions that would require package manifest changes.

    :stability: experimental
    '''
    AUTO = "AUTO"
    '''(experimental) - For apps, the version requirements are increased.

    - For libraries, the range of versions is widened.

    :stability: experimental
    '''
    WIDEN = "WIDEN"
    '''(experimental) Relax the version requirement to include both the new and old version, when possible.

    :stability: experimental
    '''
    INCREASE = "INCREASE"
    '''(experimental) Always increase the version requirement to match the new version.

    :stability: experimental
    '''
    INCREASE_IF_NECESSARY = "INCREASE_IF_NECESSARY"
    '''(experimental) Increase the version requirement only when required by the new version.

    :stability: experimental
    '''


__all__ = [
    "AutoApprove",
    "AutoApproveOptions",
    "AutoMerge",
    "AutoMergeOptions",
    "Dependabot",
    "DependabotIgnore",
    "DependabotOptions",
    "DependabotRegistry",
    "DependabotRegistryType",
    "DependabotScheduleInterval",
    "GitHub",
    "GitHubActionsProvider",
    "GitHubOptions",
    "GitHubProject",
    "GitHubProjectOptions",
    "GitIdentity",
    "GithubCredentials",
    "GithubCredentialsAppOptions",
    "GithubCredentialsPersonalAccessTokenOptions",
    "GithubWorkflow",
    "GithubWorkflowOptions",
    "IAddConditionsLater",
    "Mergify",
    "MergifyConditionalOperator",
    "MergifyOptions",
    "MergifyQueue",
    "MergifyRule",
    "PullRequestLint",
    "PullRequestLintOptions",
    "PullRequestTemplate",
    "PullRequestTemplateOptions",
    "SemanticTitleOptions",
    "Stale",
    "StaleBehavior",
    "StaleOptions",
    "TaskWorkflow",
    "TaskWorkflowOptions",
    "VersioningStrategy",
    "workflows",
]

publication.publish()

# Loading modules to ensure their types are registered with the jsii runtime library
from . import workflows

def _typecheckingstub__b9950225018303493365be2cb651e0d7d64a1e6439bed8efe63e4e98ab101e8a(
    github: GitHub,
    *,
    allowed_usernames: typing.Optional[typing.Sequence[builtins.str]] = None,
    label: typing.Optional[builtins.str] = None,
    runs_on: typing.Optional[typing.Sequence[builtins.str]] = None,
    secret: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f9c4613bc56be10f461d808c77225c1917fcd25ebccedbc39aa410ff163ca51(
    *,
    allowed_usernames: typing.Optional[typing.Sequence[builtins.str]] = None,
    label: typing.Optional[builtins.str] = None,
    runs_on: typing.Optional[typing.Sequence[builtins.str]] = None,
    secret: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a125392ca9d07df0a091430c42a2b3667d34352f1988581c1a676ea6b97b23ee(
    github: GitHub,
    *,
    approved_reviews: typing.Optional[jsii.Number] = None,
    blocking_labels: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fc6f0a71e209ec5af66ae78f6e33286352ce740d2b4f5322d49235524925962(
    *conditions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d31a0b1fd99df9d992f0152c47af38a540e5f5ced1936de9b0aa46f305ec5355(
    later: IAddConditionsLater,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8ab02e50aae05e5a55d4a4adc4369d19ed7205ed83b7ca13d32b3d6250e676a(
    *,
    approved_reviews: typing.Optional[jsii.Number] = None,
    blocking_labels: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2caae883697ce14c090e89c8fd0dbbab7e7c0f31d6d4d66311f05a6793bd9e92(
    github: GitHub,
    *,
    ignore: typing.Optional[typing.Sequence[typing.Union[DependabotIgnore, typing.Dict[builtins.str, typing.Any]]]] = None,
    ignore_projen: typing.Optional[builtins.bool] = None,
    labels: typing.Optional[typing.Sequence[builtins.str]] = None,
    registries: typing.Optional[typing.Mapping[builtins.str, typing.Union[DependabotRegistry, typing.Dict[builtins.str, typing.Any]]]] = None,
    schedule_interval: typing.Optional[DependabotScheduleInterval] = None,
    versioning_strategy: typing.Optional[VersioningStrategy] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7691a54ace72067f7bae441e5ddeb589e23479b335d208490ece30b03e170d02(
    dependency_name: builtins.str,
    *versions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e56f402ddf44883464ec12efeaccc97a7e042d533028c01db1fcda57dd3859c8(
    *,
    dependency_name: builtins.str,
    versions: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0078e67a79ce21c460b876a72b4fbd4a358306502062bdf9bdb13085805a3f2(
    *,
    ignore: typing.Optional[typing.Sequence[typing.Union[DependabotIgnore, typing.Dict[builtins.str, typing.Any]]]] = None,
    ignore_projen: typing.Optional[builtins.bool] = None,
    labels: typing.Optional[typing.Sequence[builtins.str]] = None,
    registries: typing.Optional[typing.Mapping[builtins.str, typing.Union[DependabotRegistry, typing.Dict[builtins.str, typing.Any]]]] = None,
    schedule_interval: typing.Optional[DependabotScheduleInterval] = None,
    versioning_strategy: typing.Optional[VersioningStrategy] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71dcef0810bce091e26ea45c125fc125b6b541331dd4f1fa62466d1f52b108d4(
    *,
    type: DependabotRegistryType,
    url: builtins.str,
    key: typing.Optional[builtins.str] = None,
    organization: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    replaces_base: typing.Optional[builtins.bool] = None,
    token: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65db11e8703472c7fa4e013294c649e43b7f8634b29ca11be71b46d8c549c4d1(
    project: _Project_57d89203,
    *,
    mergify: typing.Optional[builtins.bool] = None,
    mergify_options: typing.Optional[typing.Union[MergifyOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    projen_credentials: typing.Optional[GithubCredentials] = None,
    projen_token_secret: typing.Optional[builtins.str] = None,
    pull_request_lint: typing.Optional[builtins.bool] = None,
    pull_request_lint_options: typing.Optional[typing.Union[PullRequestLintOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    workflows: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1f9f6e10bd4208bf86fd269c2d9b1be37bfe497219300efebf37a151efc972e(
    project: _Project_57d89203,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4837ecd412981af090d26642873c81c7ca7b69a5c2079c390fb0d3d7168522ff(
    *content: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79e4dc466f25fa1bf920982b1e4d0a98ce7f5ac928835c4607e7f8879a2e1d06(
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f821cd3bc9db1cb000e2f440c05596f751009b48915d68cabe70e35b8d76b9b(
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24cff0cda4c3df59446abb56b6381699178c88cc41a2184a819684d64a6d343c(
    action: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20166ac47381861e1a45b550a5e9646380c52a927fca9ebf00ec36dab0f295ed(
    action: builtins.str,
    override: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c22e66f011c96f13a6f4e5b07bb676bf98b477678e968ee61f79ee107a7d2bd7(
    *,
    mergify: typing.Optional[builtins.bool] = None,
    mergify_options: typing.Optional[typing.Union[MergifyOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    projen_credentials: typing.Optional[GithubCredentials] = None,
    projen_token_secret: typing.Optional[builtins.str] = None,
    pull_request_lint: typing.Optional[builtins.bool] = None,
    pull_request_lint_options: typing.Optional[typing.Union[PullRequestLintOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    workflows: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d5a31d0302f973c0cd7ab51b14219e96872615cf2769150b28c23b8bb3a09fc(
    glob: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e987504475149e2e7d9b25ee3320e9bdd8afa45a0da64af7b3a153489524cd70(
    *,
    name: builtins.str,
    commit_generated: typing.Optional[builtins.bool] = None,
    logging: typing.Optional[typing.Union[_LoggerOptions_eb0f6309, typing.Dict[builtins.str, typing.Any]]] = None,
    outdir: typing.Optional[builtins.str] = None,
    parent: typing.Optional[_Project_57d89203] = None,
    projen_command: typing.Optional[builtins.str] = None,
    projenrc_json: typing.Optional[builtins.bool] = None,
    projenrc_json_options: typing.Optional[typing.Union[_ProjenrcOptions_164bd039, typing.Dict[builtins.str, typing.Any]]] = None,
    renovatebot: typing.Optional[builtins.bool] = None,
    renovatebot_options: typing.Optional[typing.Union[_RenovatebotOptions_18e6b8a1, typing.Dict[builtins.str, typing.Any]]] = None,
    auto_approve_options: typing.Optional[typing.Union[AutoApproveOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    auto_merge: typing.Optional[builtins.bool] = None,
    auto_merge_options: typing.Optional[typing.Union[AutoMergeOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    clobber: typing.Optional[builtins.bool] = None,
    dev_container: typing.Optional[builtins.bool] = None,
    github: typing.Optional[builtins.bool] = None,
    github_options: typing.Optional[typing.Union[GitHubOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    gitpod: typing.Optional[builtins.bool] = None,
    mergify: typing.Optional[builtins.bool] = None,
    mergify_options: typing.Optional[typing.Union[MergifyOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    project_type: typing.Optional[_ProjectType_fd80c725] = None,
    projen_credentials: typing.Optional[GithubCredentials] = None,
    projen_token_secret: typing.Optional[builtins.str] = None,
    readme: typing.Optional[typing.Union[_SampleReadmeProps_3518b03b, typing.Dict[builtins.str, typing.Any]]] = None,
    stale: typing.Optional[builtins.bool] = None,
    stale_options: typing.Optional[typing.Union[StaleOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    vscode: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9975d58a3cca9992aa51d0da1572c207d374c146dec0474fc911a56739c487e(
    *,
    email: builtins.str,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfe552d6288d1f706792afe5f041e666db050b8d0d3bb7062899a3bdefe652a8(
    *,
    app_id_secret: typing.Optional[builtins.str] = None,
    permissions: typing.Optional[typing.Union[_AppPermissions_59709d51, typing.Dict[builtins.str, typing.Any]]] = None,
    private_key_secret: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e78a929d8dcc77b9b129a8219f48eb2caa427b99d226997aadfbbccaaa8bbc1(
    *,
    secret: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca4f375b4fda039fc4fb5b2f4ad26a9d1695085d170d2d76e6d720c7cc22d02a(
    github: GitHub,
    name: builtins.str,
    *,
    concurrency: typing.Optional[builtins.str] = None,
    force: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41cabee474513917adfff8f9da118269944812886b749e97c9b0d6a0c6b27c68(
    id: builtins.str,
    job: typing.Union[typing.Union[_JobCallingReusableWorkflow_12ad1018, typing.Dict[builtins.str, typing.Any]], typing.Union[_Job_20ffcf45, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35b214ee606f61696719b92d704439e37a0a249e846714952fe087dd08b962c4(
    jobs: typing.Mapping[builtins.str, typing.Union[typing.Union[_JobCallingReusableWorkflow_12ad1018, typing.Dict[builtins.str, typing.Any]], typing.Union[_Job_20ffcf45, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6273080200c7722c9774364ee8460bccd3337cd48edc420530ca75f7c2974d9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c779b00d3df0cff3a9570cc6ed35339952399a898d5854423c3329b55bf736ec(
    *,
    concurrency: typing.Optional[builtins.str] = None,
    force: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98cefc8f23feb67fa3f26fe0afa2490919ec4c7078182e46e92ccd4220389a8c(
    github: GitHub,
    *,
    queues: typing.Optional[typing.Sequence[typing.Union[MergifyQueue, typing.Dict[builtins.str, typing.Any]]]] = None,
    rules: typing.Optional[typing.Sequence[typing.Union[MergifyRule, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c18537aa65489dcd3a6af1268daa4ec994e84f0720a3e846460acbcbf8e1474d(
    *,
    and_: typing.Optional[typing.Sequence[typing.Union[builtins.str, typing.Union[MergifyConditionalOperator, typing.Dict[builtins.str, typing.Any]]]]] = None,
    or_: typing.Optional[typing.Sequence[typing.Union[builtins.str, typing.Union[MergifyConditionalOperator, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__527734fcd5357c536553ff5f47fe5062b93958305a451f587c870879e4f2c441(
    *,
    queues: typing.Optional[typing.Sequence[typing.Union[MergifyQueue, typing.Dict[builtins.str, typing.Any]]]] = None,
    rules: typing.Optional[typing.Sequence[typing.Union[MergifyRule, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0471efd0a49bc64e556512e765a1df23d4a975f26cb6de765579b4173907f467(
    *,
    conditions: typing.Sequence[typing.Union[builtins.str, typing.Union[MergifyConditionalOperator, typing.Dict[builtins.str, typing.Any]]]],
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95405391335691b357d88cc73d37d1ee20fceae6cf671811812f639729b5accd(
    *,
    actions: typing.Mapping[builtins.str, typing.Any],
    conditions: typing.Sequence[typing.Union[builtins.str, typing.Union[MergifyConditionalOperator, typing.Dict[builtins.str, typing.Any]]]],
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e947e718bf3d7bd85f25ecd7154aeef36d789ef76012c5d50b8c1a265be7750(
    github: GitHub,
    *,
    runs_on: typing.Optional[typing.Sequence[builtins.str]] = None,
    semantic_title: typing.Optional[builtins.bool] = None,
    semantic_title_options: typing.Optional[typing.Union[SemanticTitleOptions, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__753ecd53f4dea89ebcc13327977e141a051588fef5185d3f14e06f44f6c47a63(
    *,
    runs_on: typing.Optional[typing.Sequence[builtins.str]] = None,
    semantic_title: typing.Optional[builtins.bool] = None,
    semantic_title_options: typing.Optional[typing.Union[SemanticTitleOptions, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__609f06a532384d8ff817f7118dd1e021a8ee15a4aeb1b785b674a5c885fabc7b(
    github: GitHub,
    *,
    lines: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8786063961cc00764e7c2005db60e7d427b8a81ce2275510888beb4eed1d1c6(
    *,
    lines: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d043d0484269cca19493b2d2d5c51f9cfe65a12520148f80ef37f6855457de0(
    *,
    require_scope: typing.Optional[builtins.bool] = None,
    types: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cde7a08a3b4ffe6754e0a55a7717404b9b4693c90412e433734959e936b1a9b8(
    github: GitHub,
    *,
    issues: typing.Optional[typing.Union[StaleBehavior, typing.Dict[builtins.str, typing.Any]]] = None,
    pull_request: typing.Optional[typing.Union[StaleBehavior, typing.Dict[builtins.str, typing.Any]]] = None,
    runs_on: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14e82ddb43ce0bf58c1e751d8ad775da433271157f06eea21bcdab08f1f837f1(
    *,
    close_message: typing.Optional[builtins.str] = None,
    days_before_close: typing.Optional[jsii.Number] = None,
    days_before_stale: typing.Optional[jsii.Number] = None,
    enabled: typing.Optional[builtins.bool] = None,
    exempt_labels: typing.Optional[typing.Sequence[builtins.str]] = None,
    stale_label: typing.Optional[builtins.str] = None,
    stale_message: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3522ab5e4c43b16a792a120a46122600785f2af070bebc9421e03d5a3d80e371(
    *,
    issues: typing.Optional[typing.Union[StaleBehavior, typing.Dict[builtins.str, typing.Any]]] = None,
    pull_request: typing.Optional[typing.Union[StaleBehavior, typing.Dict[builtins.str, typing.Any]]] = None,
    runs_on: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d4fb3030e96a87b921aa6bfb0d4ccf7a90d4c2affbcb8eeca2d5a24c057601c(
    github: GitHub,
    *,
    name: builtins.str,
    permissions: typing.Union[_JobPermissions_3b5b53dc, typing.Dict[builtins.str, typing.Any]],
    task: _Task_9fa875b6,
    artifacts_directory: typing.Optional[builtins.str] = None,
    checkout_with: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    condition: typing.Optional[builtins.str] = None,
    container: typing.Optional[typing.Union[_ContainerOptions_f50907af, typing.Dict[builtins.str, typing.Any]]] = None,
    env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    git_identity: typing.Optional[typing.Union[GitIdentity, typing.Dict[builtins.str, typing.Any]]] = None,
    job_id: typing.Optional[builtins.str] = None,
    outputs: typing.Optional[typing.Mapping[builtins.str, typing.Union[_JobStepOutput_acebe827, typing.Dict[builtins.str, typing.Any]]]] = None,
    post_build_steps: typing.Optional[typing.Sequence[typing.Union[_JobStep_c3287c05, typing.Dict[builtins.str, typing.Any]]]] = None,
    pre_build_steps: typing.Optional[typing.Sequence[typing.Union[_JobStep_c3287c05, typing.Dict[builtins.str, typing.Any]]]] = None,
    pre_checkout_steps: typing.Optional[typing.Sequence[typing.Union[_JobStep_c3287c05, typing.Dict[builtins.str, typing.Any]]]] = None,
    runs_on: typing.Optional[typing.Sequence[builtins.str]] = None,
    triggers: typing.Optional[typing.Union[_Triggers_e9ae7617, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15e1c594f5876baf2e105789fcb541bcb5e71cea5ad4320fb67052a9ce6946a8(
    *,
    name: builtins.str,
    permissions: typing.Union[_JobPermissions_3b5b53dc, typing.Dict[builtins.str, typing.Any]],
    task: _Task_9fa875b6,
    artifacts_directory: typing.Optional[builtins.str] = None,
    checkout_with: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    condition: typing.Optional[builtins.str] = None,
    container: typing.Optional[typing.Union[_ContainerOptions_f50907af, typing.Dict[builtins.str, typing.Any]]] = None,
    env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    git_identity: typing.Optional[typing.Union[GitIdentity, typing.Dict[builtins.str, typing.Any]]] = None,
    job_id: typing.Optional[builtins.str] = None,
    outputs: typing.Optional[typing.Mapping[builtins.str, typing.Union[_JobStepOutput_acebe827, typing.Dict[builtins.str, typing.Any]]]] = None,
    post_build_steps: typing.Optional[typing.Sequence[typing.Union[_JobStep_c3287c05, typing.Dict[builtins.str, typing.Any]]]] = None,
    pre_build_steps: typing.Optional[typing.Sequence[typing.Union[_JobStep_c3287c05, typing.Dict[builtins.str, typing.Any]]]] = None,
    pre_checkout_steps: typing.Optional[typing.Sequence[typing.Union[_JobStep_c3287c05, typing.Dict[builtins.str, typing.Any]]]] = None,
    runs_on: typing.Optional[typing.Sequence[builtins.str]] = None,
    triggers: typing.Optional[typing.Union[_Triggers_e9ae7617, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass
